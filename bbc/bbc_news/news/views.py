from django.shortcuts import render
from .scraper import scrape_top_news

def home(request):
    articles = scrape_top_news()
    return render(request, 'news/templates/home.html', {'articles': articles})

