from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Feed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .recommendations.hybrid import hybrid_recommendations
from .serializers import UserSerializer, FeedSerializer
from rest_framework.exceptions import NotFound
import jwt, datetime

class Recommendations(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'feedme', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.get(id=payload['id'])
        
        hybrid_recommendations(user.id)
        recommendations = user.recommendations.all()
        
        serializer = FeedSerializer(recommendations, many=True)
        
        return Response(serializer.data)

class MarkArticle(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
            
        if not token:
            raise AuthenticationFailed('Unauthenticated')
            
        try:
            payload = jwt.decode(token, 'feedme', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user_id = payload['id']
        feed_id = request.data['feed_id']
        
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
        return Response("article read!")

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
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': "success"
        }
        
        return response
    
class Newsfeed(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
    
        category = request.query_params.get('category')
        
        newsfeed = Feed.objects.filter(category=category).order_by('-date')[:20]
        
        if not newsfeed:
            raise NotFound('No newsfeed found for the specified category')
        
        serializer = FeedSerializer(newsfeed, many=True)

        return Response(serializer.data)
        
        