from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/', views.Recommendations.as_view()),
    path('mark_read/', views.mark_article_as_read),
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('user/', views.UserView.as_view()),
    path('logout/', views.Logout.as_view()),
]
