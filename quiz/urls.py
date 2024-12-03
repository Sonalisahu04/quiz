# quiz/urls.py
from django.urls import path
from .views import *



urlpatterns = [
    path('', Quiz, name='Quiz'),
    path('submit_quiz/', submit_quiz, name='submit_quiz'),
]
