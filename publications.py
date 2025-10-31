import arxiv
import re

# Paramètres
author = "Nicolas Gilliers"
max_results = 50  

# Requête arXiv : 
query = f"au:{author}"

search = arxiv.Search(
    query=query,
    max_results=max_results,
    sort_by=arxiv.SortCriterion.SubmittedDate
)


markdown_lines = []

for result in search.results():
    title = result.title.replace("\n", " ")
    authors = ", ".join([a.name for a in result.authors])
    url = result.entry_id
    published = result.published.strftime("%Y‑%m‑%d")
    summary = re.sub(r"\s+", " ", result.summary).strip()

    markdown_lines.append(f"## {title}\n")
    markdown_lines.append(f"- **Auteurs** : {authors}\n")
    markdown_lines.append(f"- **Date de soumission** : {published}\n")
    markdown_lines.append(f"- **URL** : [{url}]({url})\n")
    markdown_lines.append(f"- **Résumé** : {summary}\n")
    markdown_lines.append("\n---\n")

# Écriture du fichier
with open("publications_gilliers.md", "w", encoding="utf‑8") as f:
    f.write("\n".join(markdown_lines))

html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])

html_page = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Publications Nicolas Gilliers</title>
<style>
body {{ font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 2em; }}
h1, h2 {{ color: #2c3e50; }}
hr {{ margin: 2em 0; }}
</style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Écriture du fichier HTML
with open("publications_gilliers.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("Fichiers publications_gilliers.md et publications_gilliers.html créés avec succès.")
