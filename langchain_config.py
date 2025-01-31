import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Specify the model name explicitly
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def get_news_articles(query=""):
    if query:
        url = f"https://timesofindia.indiatimes.com/topic/{query}"
    else:
        url = "https://timesofindia.indiatimes.com/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    if query:
        # Update with the actual HTML structure
        for item in soup.find_all('div', class_='search-result'):
            headline = item.find('span', class_='title')
            summary = item.find('div', class_='snippet')
            if headline and summary:
                articles.append({
                    'title': headline.get_text(strip=True),
                    'description': summary.get_text(strip=True)
                })
    else:
        # Update with the actual HTML structure
        for item in soup.find_all('div', class_='content'):
            headline = item.find('span', class_='w_tle')
            summary = item.find('span', class_='w_desc')
            if headline and summary:
                articles.append({
                    'title': headline.get_text(strip=True),
                    'description': summary.get_text(strip=True)
                })
    
    return articles

def summarize_articles(articles):
    summaries = []
    for article in articles:
        content = article['description']
        if content:
            # Summarize the article content
            summary = summarizer(content, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
            summaries.append(summary)
    return summaries