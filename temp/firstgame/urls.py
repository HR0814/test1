from django.urls import path
from . import views

urlpatterns = [
    path('game1/', views.game1),
    path('test/', views.test),
    path('start/', views.start),
    path('testmusic/', views.testmusic),
    path('wordquiz/', views.wordquiz),
    path('wordanswer/', views.wordanswer),
    path('musicquiz/', views.musicquiz),
    path('musicanswer/', views.musicanswer),
    path('quiz/home', views.home),
    path('insert/', views.insert),
]
