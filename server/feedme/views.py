from django.shortcuts import render
from django.http import HttpResponse
# from .models import Newsletter, User
from google_news_feed import GoogleNewsFeed
from newsplease import NewsPlease
from newspaper import Source

def fetch_google_news_feed(request):
    
    cnn_paper = Source("https://thestar.com")
    
    cnn_paper.clean_memo_cache()
    
    cnn_paper.build()


    links = cnn_paper.article_urls()
    
    articles = NewsPlease.from_urls(links[:10])
    
    print(articles)
    
    for article in articles.values():
        print(article.date_publish)
        print(article.title)
        
    articles_string = "\n".join([f"{article.title}" for article in articles.values()])
    
    # Return the articles as an HTTP response
    return HttpResponse(articles_string)

