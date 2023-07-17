from django.urls import path
from .views import show_articles_categories, show_article, hello

urlpatterns = [
    path('hello', hello),
    path('articles/', show_articles_categories),
    path('article/<article>', show_article),
]
