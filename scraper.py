import requests
from bs4 import BeautifulSoup

def get_news_articles(query):
    url = f"https://timesofindia.indiatimes.com/topic/{query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []

    for item in soup.find_all('div', class_='search-item'):
        headline = item.find('span', class_='title')
        summary = item.find('div', class_='content')
        if headline and summary:
            articles.append({
                'title': headline.get_text(strip=True),
                'description': summary.get_text(strip=True)
            })
    return articles

if __name__ == "__main__":
    query = "Olympics"  # Example query
    articles = get_news_articles(query)
    for i, article in enumerate(articles, start=1):
        print(f"Article {i}:")
        print(f"Title: {article['title']}")
        print(f"Summary: {article['description']}")
        print()