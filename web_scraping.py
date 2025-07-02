import feedparser
import csv
import os

url = "https://feeds.feedburner.com/TheHackersNews"
feed = feedparser.parse(url)

if feed.bozo:
    print("Erro ao carregar o feed:", feed.bozo_exception)
else:
    os.makedirs("result-web-scraping", exist_ok=True)
    with open("result-web-scraping/noticias_hackernews_rss.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Título", "Link", "Resumo"])
        for entry in feed.entries:
            titulo = entry.title
            link = entry.link
            resumo = entry.summary if 'summary' in entry else ""
            writer.writerow([titulo, link, resumo])

    print(f"Total de notícias salvas: {len(feed.entries)}")
    print("Notícias salvas em result-web-scraping/noticias_hackernews_rss.csv")
