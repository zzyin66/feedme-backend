from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Feed
from google_news_feed import GoogleNewsFeed
from newsplease import NewsPlease
from newspaper import Source
from datetime import date, timedelta
from .recommendations.hybrid import hybrid_recommendations
import json

def fetch_google_news_feed(request):
    #User.objects.create(username="test", password="1234", email="test@test.com", keywords={})
    #User.objects.create(username="test2", password="1234", email="test2@test.com", keywords={})
    return HttpResponse("hello world")

def recommendations(request):
    hybrid_recommendations("7074d947082441f49f8818d08069fd32")
    user = User.objects.get(id="7074d947082441f49f8818d08069fd32")
    
    recommendations = user.recommendations.all()
    
    context = {'recommendations': recommendations}

    return render(request, 'recommendations_template.html', context)

def mark_article_as_read(request):
    
    request_data = json.loads(request.body)
    
    user_id = request_data['user_id']
    feed_id = request_data['feed_id']
    
    try:
        user = User.objects.get(id=user_id)
        feed = Feed.objects.get(id=feed_id)
        user_keywords = user.keywords
        feed_keywords = feed.keywords
        
        updated_keywords = user_keywords.copy()
        
        for key, value in feed_keywords.items():
            if key in updated_keywords:
                key_value = updated_keywords[key]
                updated_keywords[key] += float(value) + float(key_value)
            else:
                updated_keywords[key] = float(value)   

        
        user.keywords = updated_keywords
        user.feed_history.add(feed_id)
        user.save()
    except:
        pass    
    return HttpResponse("read this article")
    
