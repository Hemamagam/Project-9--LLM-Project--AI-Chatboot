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