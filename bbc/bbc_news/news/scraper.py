from bs4 import BeautifulSoup
import requests

def scrape_top_news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []
    for article in soup.find_all('article', class_='gs-c-promo'):
        title = article.find('h3', class_='gs-c-promo-heading__title').text.strip()
        summary = article.find('p', class_='gs-c-promo-summary').text.strip()
        image_url = article.find('img')['src']
        articles.append({
            'title': title,
            'summary': summary,
            'source': 'BBC News',
            'image_url': image_url,
        })
    return articles
