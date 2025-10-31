import arxiv
import re
import markdown2

# Paramètres
author = "Gilliers"
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
    
print("Fichiers publications_gilliers.md et publications_gilliers.html créés avec succès.")
