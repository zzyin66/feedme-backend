from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Feed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .recommendations.hybrid import hybrid_recommendations
from .serializers import UserSerializer
import jwt, datetime
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

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        

        payload = {
            'id': str(user.id),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=3),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'feedme', algorithm='HS256')
        
        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'feedme', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.get(id=payload['id'])
        serializer = UserSerializer(user)
        
        return Response(serializer.data)
    
class Logout(APIView):
    def post(self, request):
        response = Response
        response.delete_cookie('jwt')
        response.data = {
            'message': "success"
        }
        
        return response