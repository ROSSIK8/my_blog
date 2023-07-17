from django.contrib import admin
from django.urls import path
from .views import show_articles_categories, show_article

urlpatterns = [
    path('articles/', show_articles_categories),
    path('article/<article>', show_article),
]
