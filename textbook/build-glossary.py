import re
import yaml
from pathlib import Path
from collections import defaultdict
import os

chapter_base_dir = Path("textbook/")
output_file = chapter_base_dir / "glossary.md"
output_code_file = chapter_base_dir / "code-glossary.md"
toc_path = chapter_base_dir / "_toc.yml"

# --- TOC parsing with recursive section handling ---
def collect_files(section_list, chapter_num, chapter_to_files):
    for section in section_list:
        section_file = section.get("file")
        if section_file:
            chapter_to_files[chapter_num].append(section_file)
        if "sections" in section:
            collect_files(section["sections"], chapter_num, chapter_to_files)

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
def sort_key(heading_line):
    heading_text = heading_line.strip()
    heading_text = re.sub(r'^##\s*`?(.*?)`?\s*$', r'\1', heading_text)
    heading_text = heading_text.lower()
    heading_text = re.sub(r'^(a|an|the)\s+', '', heading_text)
    return heading_text

# --- Parse glossary entries ---
def parse_entries(files):
    term_map = {}
    for file in files:
        lines = file.read_text().splitlines()
        current = []
        for line in lines:
            if line.startswith("## "):
                if current:
                    key = sort_key(current[0])
                    term_map[key] = (current, file)
                current = [line]
            else:
                current.append(line)
        if current:
            key = sort_key(current[0])
            term_map[key] = (current, file)
    return term_map

# --- Summarize for "New in This Chapter" ---
def slugify(term):
    # Lowercase, remove non-word characters except space, hyphen, underscore, then replace spaces with hyphens
    return re.sub(r'[^\w\s-]', '', term.strip()).lower().replace(" ", "-")

def summarize_entries(entries, glossary_filename):
    summary = []
    for entry, _ in sorted(entries.values(), key=lambda e: sort_key(e[0][0])):
        if not entry:
            continue
        title_line = entry[0]
        # Extract and clean term (strip ##, backticks, whitespace)
        term_raw = title_line.replace("##", "").strip().strip("`")
        slug = slugify(term_raw)

        summary.append(f'<li><a href="{glossary_filename.replace(".md",".html")}#{slug}">{term_raw}</a></li>')
    # Wrap in unordered list
    return ["<ul>"] + summary + ["</ul>"]


# --- Insert summary into chapter file ---
def insert_at_end_of_file(file_path, term_links, code_links):
    marker_start = "<!-- NEW_TERMS_START -->"
    marker_end = "<!-- NEW_TERMS_END -->"

    rel_glossary = os.path.relpath(chapter_base_dir / "glossary.html", start=file_path.parent)
    rel_code_glossary = os.path.relpath(chapter_base_dir / "code-glossary.html", start=file_path.parent)

    # block = ["\n", marker_start]
    # #block += [":::{margin}"]
    # block += [":::{admonition} New in This Chapter", ":class: tip"]
    # block += ["**Terms**"] + term_summary
    # block += ["**Code**"] + code_summary
    # #block += [":::", "\n"]
    # block += [":::", marker_end, "\n"]
    
    block = f"""
    <!-- NEW_TERMS_START -->
    ```html
    <div class="admonition tip" name="html-admonition" style="background-color:#800000; color:white; padding:1em; border-radius:6px;">
    <p class="title">New in This Chapter</p>
    <div style="display: flex; gap: 2em; margin-top: 1em;">
        <div>
        <h4>Terms</h4>
        <ul>
            {''.join(f'<li><a href="{rel_glossary}#{slug}" style="color:white;">{term}</a></li>' for term, slug in term_links)}
        </ul>
        </div>
        <div>
        <h4>Code</h4>
        <ul>
            {''.join(f'<li><a href="{rel_code_glossary}#{slug}" style="color:white;">{term}</a></li>' for term, slug in code_links)}
        </ul>
        </div>
    </div>
    </div>
    ```
    <!-- NEW_TERMS_END -->
    """

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
                content = re.sub(
                    f"{marker_start}.*?{marker_end}",
                    block,
                    content,
                    flags=re.DOTALL
                )
            else:
                content = content.rstrip() + block
            file_path.write_text(content)

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
        term_file = next(Path(chapter_base_dir / chapter).rglob("*-glossary.md"), None)
        code_file = next(Path(chapter_base_dir / chapter).rglob("*-code-glossary.md"), None)

        term_entries = parse_entries([term_file]) if term_file else {}
        code_entries = parse_entries([code_file]) if code_file else {}

        if term_entries or code_entries:
            term_links = [(entry[0].replace("##", "").strip().strip("`"), slugify(entry[0].replace("##", "").strip().strip("`")))
              for entry, _ in sorted(term_entries.values(), key=lambda e: sort_key(e[0][0]))]

            code_links = [(entry[0].replace("##", "").strip().strip("`"), slugify(entry[0].replace("##", "").strip().strip("`")))
                        for entry, _ in sorted(code_entries.values(), key=lambda e: sort_key(e[0][0]))]


            global_terms.update(term_entries)
            global_code_terms.update(code_entries)

            insert_at_end_of_file(last_file, term_links, code_links)


    return global_terms, global_code_terms

# --- Global glossary builder ---
def build_global_glossary(entries, top_anchor, output_path, title, preserve_case=False):
    entries_by_letter = defaultdict(list)
    for key, (entry, file) in entries.items():
        first_char = key[0].upper()
        if not first_char.isalpha():
            first_char = "\\\#@"  # Group symbols/numbers
        entries_by_letter[first_char].append((entry, file))

    all_letters = sorted(entries_by_letter.keys(), key=lambda x: (x == "#", x))
    index = "| ".join(
        f"[{letter}]({'other' if letter == '\\\#@' else letter.lower()})"
        for letter in all_letters
    ) + "\n\n"

    with output_path.open("w") as f:
        f.write(f"({top_anchor})=\n# {title}\n\n")
        f.write("<!-- AUTO-GENERATED: Do not edit this file directly -->\n\n")
        f.write("## Index\n\n" + index)

        for letter in all_letters:
            anchor = letter.lower() if letter.isalpha() else "other"
            f.write(f"({anchor})=\n## {letter} \n\n")

            for entry, file in sorted(entries_by_letter[letter], key=lambda ef: sort_key(ef[0][0])):
                # Resolve chapter link
                parts = file.relative_to(chapter_base_dir).parts
                chapter = parts[0] if parts else None
                link = ""
                if chapter and chapter in chapter_to_files[chapter]:
                    link = (
                        f"\n<span style='font-size:smaller'>Learn more in "
                        f"[Chapter {chapter.lstrip('0')}]({chapter_to_files[chapter]}), "
                    )

                # Format heading
                heading = entry[0]
                display_term = heading.replace("##", "").strip()
                #display_term = term_raw.strip("` ")
                if any(c in display_term for c in ['`', '\\', '"', "'"]):
                    entry[0] = f"### ``{display_term}``"
                else:
                    entry[0] = f"### {display_term}"
                if not preserve_case:
                    display_term = display_term.title()
                entry[0] = f"### {display_term}"

                # Add footer links
                if link:
                    entry.append(link)
                entry.append(f"[Back to Top]({top_anchor})")

                f.write("\n".join(entry).strip() + "\n\n")

# --- Run everything ---
terms, code_terms = process_chapter_glossaries()
build_global_glossary(terms, "index", output_file, "Glossary of Terms", preserve_case=False)
build_global_glossary(code_terms, "code-index", output_code_file, "Glossary of Code", preserve_case=True)