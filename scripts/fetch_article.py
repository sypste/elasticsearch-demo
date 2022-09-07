import wikipedia
import json

article = wikipedia.page('Michael Jordan')
article.summary

with open(f'_articles/{article.title}.json', 'w', encoding='utf-8') as write_file:
    json.dump({
        'url': article.url,
        'title': article.title,
        'summary': article.summary,
        'content': article.content,
        'links': article.links
    }, write_file, ensure_ascii=False)
