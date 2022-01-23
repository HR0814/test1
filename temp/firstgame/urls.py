from django.urls import path
from . import views

urlpatterns = [
    path('game1/', views.game1),
    path('test/', views.test),
    path('testmusic/', views.testmusic),
    path('quiz/', views.quiz),
    path('answer/', views.answer),
]