from django.urls import path
from . import views

urlpatterns = [
    path('news_feed/', views.fetch_google_news_feed, name='news_feed'),
]
