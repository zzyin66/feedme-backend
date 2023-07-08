from django.shortcuts import render
from django.http import HttpResponse
# from .models import Newsletter, User
from google_news_feed import GoogleNewsFeed
from newsplease import NewsPlease
from newsplease import NewsArticle

def fetch_google_news_feed(request):
    gn = GoogleNewsFeed(language="en", country="CA", resolve_internal_links=True)
    top_results = gn.top_headlines()
    links = [result.link for result in top_results]
    articles = []
    for link in links:
        article = NewsPlease.from_url(link)
        print(article)
        articles.append(article)
        
    articles_string = "\n".join([f"{article.title} \n" for article in articles])
    
    # Return the articles as an HTTP response
    return HttpResponse(articles_string)

