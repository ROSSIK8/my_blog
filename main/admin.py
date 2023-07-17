from django.contrib import admin
from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']


# @admin.register(CategoryArticle)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['article', 'category']

