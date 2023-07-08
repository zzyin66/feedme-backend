from django.shortcuts import render
from .models import Newsletter, User
from google_news_feed import GoogleNewsFeed
from newsplease import NewsPlease
from newsplease import NewsArticle

def fetch_google_news_feed():
    gn = GoogleNewsFeed(language="en", country="CA", resolve_internal_links=True)
    top_results = gn.top_headlines()
    links = [result.link for result in top_results]
    articles = []
    for link in links:
        article = NewsPlease.from_url(link)
        articles.append(article)
    return articles

