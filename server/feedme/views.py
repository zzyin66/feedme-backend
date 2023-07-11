from django.shortcuts import render
from django.http import HttpResponse
# from .models import Newsletter, User
from google_news_feed import GoogleNewsFeed
from newsplease import NewsPlease
from newspaper import Source

def fetch_google_news_feed(request):
    gn = GoogleNewsFeed(language="en", country="CA", resolve_internal_links=True)
    
    for category in ["world"]:
        results = gn.query_topic(category)
        links = [result.link for result in results]
        
        # article = ""
        try:
            article = NewsPlease.from_url(links[0], timeout=5)
        except:
            pass
        
        # for link in links:
        #     try:
        #         print(link)
        #         article = NewsPlease.from_url(link, timeout=5)
        #     except:
        #         pass
        
        # for article in articles.values():
        #     if article.title is None or article.description is None or article.maintext is None:
        #         pass
    
    # Return the articles as an HTTP response
    return HttpResponse(article.title + " " + article.maintext)

