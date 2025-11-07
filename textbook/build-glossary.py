import re
import yaml
from pathlib import Path
from collections import defaultdict
import os

chapter_base_dir = Path("textbook/")
output_file = chapter_base_dir / "glossary.md"
output_code_file = chapter_base_dir / "code-glossary.md"
toc_path = chapter_base_dir / "_toc.yml"

def find_terms_glossary(chapter_dir: str):
    root = chapter_base_dir / chapter_dir
    for p in root.rglob("*-glossary.md"):
        name = p.name.lower()
        if name.endswith("-code-glossary.md"):
            continue                      # <-- exclude code glossary
        if name.endswith("-glossary.md"):
            return p
    return None

def find_code_glossary(chapter_dir: str):
    root = chapter_base_dir / chapter_dir
    for p in root.rglob("*-code-glossary.md"):
        if p.name.lower().endswith("-code-glossary.md"):
            return p
    return None

def extract_chapter_files(toc_file):
    with toc_file.open() as f:
        toc = yaml.safe_load(f)

    chapter_to_files = defaultdict(list)

    for part in toc.get("parts", []):
        for chap in part.get("chapters", []):
            file_stub = chap.get("file")
            if not file_stub:
                continue

            m = re.match(r"(\d+)", file_stub)
            if not m:
                continue
            chap_num = m.group(1)

            # resolve this file stub to a real .ipynb or .md
            for ext in (".ipynb", ".md"):
                p = chapter_base_dir / (file_stub + ext)
                if p.exists():
                    chapter_to_files[chap_num].append(p)
                    break

            # now walk nested sections recursively
            def walk(sections):
                for sec in sections:
                    stub = sec.get("file")
                    if stub:
                        for ext in (".ipynb", ".md"):
                            p = chapter_base_dir / (stub + ext)
                            if p.exists():
                                chapter_to_files[chap_num].append(p)
                                break
                    if "sections" in sec:
                        walk(sec["sections"])

            if "sections" in chap:
                walk(chap["sections"])

    return chapter_to_files

chapter_to_files = extract_chapter_files(toc_path)

# --- Sorting function ---
# def sort_key(heading_line):
#     heading_text = heading_line.strip()
#     heading_text = re.sub(r'^##\s*`?(.*?)`?\s*$', r'\1', heading_text)
#     heading_text = heading_text.lower()
#     heading_text = re.sub(r'^(a|an|the)\s+', '', heading_text)
#     return heading_text

def sort_key(heading_line):
    text = heading_line.strip()
    text = re.sub(r'^\s*#+\s*', '', text)   # drop any leading ##, ###, etc.
    text = text.replace('`', '')            # ignore backticks for sorting
    text = text.lower()
    text = re.sub(r'^(a|an|the)\s+', '', text)
    return text

def parse_entries(files):
    term_map = {}
    for file in files:
        lines = file.read_text().splitlines()
        current = []
        for line in lines:
            if line.startswith("## "):
                if current:
                    key = sort_key(current[0])
                    if key not in term_map:  # only add if not already in map
                        term_map[key] = (current, file)
                current = [line]
            else:
                current.append(line)
        if current:
            key = sort_key(current[0])
            if key not in term_map:  # only add if not already in map
                term_map[key] = (current, file)
    return term_map

# --- Summarize for "New in This Chapter" ---
def slugify(term):
    s = re.sub(r'[^\w\s-]', '', term.strip()).lower()
    s = re.sub(r'[\s_-]+', '-', s)
    return s.strip('-')

def term_display_and_slug(heading_line):
    """
    heading_line: e.g., '## `math` library'
    Returns:
      display_term: exact heading text without the leading '##' (keeps backticks/escapes)
      slug: cleaned for anchors (no backticks, unescaped sequences)
    """
    # Keep display exactly as authored (minus leading ##)
    display = heading_line.lstrip('#').strip()

    # Build a cleaned version for the slug: remove backticks, then unescape \" \_ \(
    cleaned = display.replace('`', '')
    cleaned = re.sub(r'\\(.)', r'\1', cleaned)  # turn \" -> ", \_ -> _, etc.

    return display, slugify(cleaned)

# --- Insert summary into chapter file ---
def insert_at_end_of_file(file_path, term_links, code_links):
    marker_start = "<!-- NEW_TERMS_START -->"
    marker_end = "<!-- NEW_TERMS_END -->"

    # If nothing to show, remove old block (if present) and return
    if not term_links and not code_links:
        if file_path.exists() and file_path.suffix == ".md":
            content = file_path.read_text()
            if marker_start in content and marker_end in content:
                content = re.sub(f"{re.escape(marker_start)}.*?{re.escape(marker_end)}", "", content, flags=re.DOTALL)
                file_path.write_text(content.strip() + "\n")
        elif file_path.exists() and file_path.suffix == ".ipynb":
            import nbformat
            nb = nbformat.read(file_path, as_version=4)
            nb.cells = [c for c in nb.cells if marker_start not in c.get("source", "")]
            nbformat.write(nb, file_path)
        return

    rel_glossary = os.path.relpath(chapter_base_dir / "glossary.html", start=file_path.parent)
    rel_code_glossary = os.path.relpath(chapter_base_dir / "code-glossary.html", start=file_path.parent)

    def html_escape(s):
        return (s.replace("&", "&amp;")
                 .replace("<", "&lt;")
                 .replace(">", "&gt;")
                 .replace('"', "&quot;")
                 .replace("'", "&#39;"))

    def html_with_code_spans(s: str) -> str:
        parts, last = [], 0
        for m in re.finditer(r'`([^`]+)`', s):
            parts.append(html_escape(s[last:m.start()]))
            parts.append(f"<code>{html_escape(m.group(1))}</code>")
            last = m.end()
        parts.append(html_escape(s[last:]))
        return ''.join(parts)

    # Build only the sections we actually have
    sections = []
    if term_links:
        terms_html = f"""
        <div>
          <h4 style="margin:.25rem 0 .4rem; font-size:1rem; font-weight:700;">
            <span style="border-bottom:2px solid rgba(128,0,0,.55); padding-bottom:2px;">Terms</span>
          </h4>
          <ul style="margin:0; padding-left:1.2rem;">
            {''.join(f'<li><a href="{rel_glossary}#{slug}" style="color:inherit; text-decoration:underline;">{html_with_code_spans(term)}</a></li>' for term, slug in term_links)}
          </ul>
        </div>
        """
        sections.append(terms_html)

    if code_links:
        code_html = f"""
        <div>
          <h4 style="margin:.25rem 0 .4rem; font-size:1rem; font-weight:700;">
            <span style="border-bottom:2px solid rgba(128,0,0,.55); padding-bottom:2px;">Code</span>
          </h4>
          <ul style="margin:0; padding-left:1.2rem;">
            {''.join(f'<li><a href="{rel_code_glossary}#{slug}" style="color:inherit; text-decoration:underline;">{html_with_code_spans(term)}</a></li>' for term, slug in code_links)}
          </ul>
        </div>
        """
        sections.append(code_html)

    block = f"""```{{raw}} html
{marker_start}
<div style="border-left:6px solid #800000; background: rgba(255,255,255,0.06) !important; box-shadow:none !important; padding:1rem; border-radius:10px; margin:1rem 0;">
  <div style="display:flex; align-items:center; gap:.6rem; margin-bottom:.6rem;">
    <span style="display:inline-block; font-weight:700; padding:.25rem .6rem; border:1px solid #800000; border-radius:.5rem; background:rgba(128,0,0,.25); color:inherit;">
      New in This Chapter
    </span>
  </div>

  <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:1.25rem; align-items:start;">
    {''.join(sections)}
  </div>
</div>
{marker_end}
```
"""
    # write/replace block as before
    if file_path.exists():
        if file_path.suffix == ".ipynb":
            import nbformat
            nb = nbformat.read(file_path, as_version=4)
            nb.cells = [cell for cell in nb.cells if marker_start not in cell.get("source", "")]
            nb.cells.append(nbformat.v4.new_markdown_cell(block))
            nbformat.write(nb, file_path)
        elif file_path.suffix == ".md":
            content = file_path.read_text()
            if marker_start in content and marker_end in content:
                content = re.sub(f"{re.escape(marker_start)}.*?{re.escape(marker_end)}",
                                block, content, flags=re.DOTALL)
            else:
                content = content.rstrip() + "\n\n" + block + "\n"
            file_path.write_text(content)

def find_exact_suffix(chapter_dir: str, suffix: str):
    """Return the first file in chapter_dir whose *name* ends exactly with suffix."""
    root = chapter_base_dir / chapter_dir
    for p in root.rglob(f"*{suffix}"):
        if p.name.endswith(suffix):
            return p
    return None

# --- Process all chapters ---
def process_chapter_glossaries():
    global_terms = {}
    global_code_terms = {}

    for chapter, files in sorted(chapter_to_files.items()):
        # files is a list of Path objects, in TOC order
        if not files:
            continue

        # last file in chapter
        last_file = files[-1]

        # your existing glossary logic:
        term_file = find_terms_glossary(chapter)
        code_file = find_code_glossary(chapter)


        term_entries = parse_entries([term_file]) if term_file else {}
        code_entries = parse_entries([code_file]) if code_file else {}

        if term_entries or code_entries:
            term_links = []
            for entry, _ in sorted(term_entries.values(), key=lambda e: sort_key(e[0][0])):
                display, slug = term_display_and_slug(entry[0])
                term_links.append((display, slug))

            code_links = []
            for entry, _ in sorted(code_entries.values(), key=lambda e: sort_key(e[0][0])):
                display, slug = term_display_and_slug(entry[0])
                code_links.append((display, slug))

            for k, v in term_entries.items():
                global_terms.setdefault(k, v)
            for k, v in code_entries.items():
                global_code_terms.setdefault(k, v)
            # global_terms.update(term_entries)
            # global_code_terms.update(code_entries)

            insert_at_end_of_file(last_file, term_links, code_links)


    return global_terms, global_code_terms

# --- Global glossary builder ---
def build_global_glossary(entries, top_anchor, output_path, title, preserve_case=False, anchor_prefix=""):
    entries_by_letter = defaultdict(list)
    for key, (entry, file) in entries.items():
        first_char = (key[0].upper() if key else "#")
        if not first_char.isalpha():
            first_char = "#"
        entries_by_letter[first_char].append((entry, file))

    all_letters = sorted(entries_by_letter.keys(), key=lambda x: ("#" in x, x))
    index = "| ".join(f"[{letter}]({'other' if letter == '#' else letter.lower()})" for letter in all_letters) + "\n\n"

    with output_path.open("w") as f:
        f.write(f"({anchor_prefix}{top_anchor})=\n# {title}\n\n")
        f.write("<!-- AUTO-GENERATED: Do not edit this file directly -->\n\n")
        f.write("## Index\n\n" + index)

        for letter in all_letters:
            anchor = "other" if letter == "#" else letter.lower()
            f.write(f"({anchor_prefix}{anchor})=\n## {letter}\n\n")

            for entry, file in sorted(entries_by_letter[letter], key=lambda ef: sort_key(ef[0][0])):
                # --- Resolve chapter folder (top-level under textbook/) ---
                try:
                    parts = file.relative_to(chapter_base_dir).parts
                except Exception:
                    parts = file.parts  # fallback if already relative

                chapter_folder = parts[0] if parts else None

                # Extract numeric chapter key (e.g., "01" from "01-intro")
                chap_key = None
                chap_num_display = None
                if chapter_folder:
                    m = re.match(r"(\d+)", chapter_folder)
                    if m:
                        chap_key = m.group(1)           # e.g., "01" (matches dict key)
                        chap_num_display = int(chap_key)  # e.g., "1" for display
                        chap_num_minus_one = chap_num_display - 1

                # First file in this chapter (from TOC order)
                chapter_first = None
                if chap_key and chap_key in chapter_to_files:
                    for p in chapter_to_files[chap_key]:
                        if p.suffix in (".md", ".ipynb"):
                            chapter_first = p
                            break

                # Build "Learn more" link if we have a target
                link_html = ""
                if chapter_first is not None and chap_num_display is not None:
                    chapter_first_html = chapter_first.with_suffix(".html")
                    rel = os.path.relpath(chapter_first_html, start=output_path.parent).replace(".ipynb",".html").replace(".md",".html")
                    link_html = f'Learn more in <a href="{rel}" style="color:inherit; text-decoration:underline;">Chapter {chap_num_display}</a>'

                # Heading text
                display_term, slug = term_display_and_slug(entry[0])

                # Optional title-casing: only when there are NO backticks,
                # so we don't break inline code like `math` or partial `math` library
                if not preserve_case and '`' not in display_term:
                    display_term = display_term.title()


                body = "\n".join(entry[1:]).strip()
                f.write(f"({slug})=\n### {display_term}\n\n")
                if body:
                    f.write(body + "\n\n")

                # Single-line footer: "Learn more in Chapter X | Back to Top"
                if link_html:
                    combined = f"{link_html} &nbsp;|&nbsp; [Back to Top]({top_anchor})"
                else:
                    combined = f"[Back to Top]({top_anchor})"
                f.write(combined + "\n\n")


# --- Run everything ---
terms, code_terms = process_chapter_glossaries()
build_global_glossary(terms, "index", output_file, "Glossary of Terms", preserve_case=False)
build_global_glossary(code_terms, "code-index", output_code_file, "Glossary of Code", preserve_case=True, anchor_prefix="code-")
