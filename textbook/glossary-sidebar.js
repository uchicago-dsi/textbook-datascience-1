document.addEventListener("DOMContentLoaded", function () {
  const glossary = document.getElementById("my-glossary");
  const sidebar = document.querySelector(".bd-sidebar-secondary");

  if (glossary && sidebar) {
    sidebar.appendChild(glossary);
  }
});