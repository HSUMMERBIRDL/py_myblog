from django.http import HttpResponse
from django.shortcuts import render

from . import models


# Create your views here.

def index(request):
    # return HttpResponse('hello python')
    # return render(request,'index.html')
    # return render(request,'blog/index.html',{"name":"huliang is studing python/django"})

    # article = models.Article.objects.get(pk=5)
    # return render(request,'blog/index.html',{"article":article})
    print 'hello ewewe'
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {"articles": articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article.html', {"article": article})


def article_edit(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/article_edit.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_edit.html', {"article": article})


def edit_action(request):
    id = request.POST.get('article_id', '0')
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    if id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {"articles": articles})
    article = models.Article.objects.get(pk=id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article.html', {"article": article})
