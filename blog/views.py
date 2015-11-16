from django.http import Http404
from django.shortcuts import render
from .models import Entry


def overview(request, category="Allgemein"):
    try:
        #category = Category.objects.filter(name=category)
        entries = Entry.objects.all()

    except Entry.DoesNotExist:
        raise Http404("Diese Beiträge konnten leider nicht gefunden werden.")
    return render(request, 'blog/overview.html',
                  {'posts':     entries,
                   #'category':  category[0]
                   })


def year(request, year):
    try:
        entries = Entry.objects.filter(created__year=year)
    except Entry.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'blog/list.html', {'entries': entries})



def month(request, year, month):
    try:
        entries = Entry.objects.filter(created__year=year,
                                       created__month=month)
    except Entry.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'blog/list.html', {'entries': entries})



def day(request, year, month, day):
    try:
        entries = Entry.objects.filter(created__year=year,
                                       created__month=month,
                                       created__day=day)
    except Entry.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'blog/list.html', {'entries': entries})
