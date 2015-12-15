from django.shortcuts import render, get_object_or_404, get_list_or_404
from articles.models import Article, Comment


def index(request):
    articles = get_list_or_404(Article.objects.order_by('-created'))
    return render(request, 'articles/list.html', {"articles": articles})


def details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article)
    return render(request, 'articles/detail.html', {"article": article,
                                                    "comments": comments})