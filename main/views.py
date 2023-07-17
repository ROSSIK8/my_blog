from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Category


def show_articles_categories(requests):
    category = Category.objects.get(title=requests.GET.get('category',
                                                           'Все статьи'))
    template = 'main/all_categories.html'
    categories = Category.objects.order_by('id')
    context = {'categories': categories,
               'category': category}
    return render(requests, template, context)


def show_article(requests, article):
    template = 'main/article_page.html'
    article_page_ = Article.objects.filter(title=article)
    context = {'article': article_page_[0]}
    return render(requests, template, context)


def hello(requests):
    return HttpResponse('Hello')
