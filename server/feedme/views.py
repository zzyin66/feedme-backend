from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Feed
from google_news_feed import GoogleNewsFeed
from newsplease import NewsPlease
from newspaper import Source
from datetime import date, timedelta
from .recommendations.content import generate_content_recommendations
import json

def fetch_google_news_feed(request):
    #User.objects.create(username="test", password="1234", email="test@test.com", keywords={})
    return HttpResponse("hello world")

def recommendations(request):
    generate_content_recommendations("583c3e76c4a74e0bbcdd433fa55cd876")
    user = User.objects.get(id="583c3e76c4a74e0bbcdd433fa55cd876")
    
    recommendations = user.reccomendations.all()
    
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
    
