from django.http import Http404
from django.shortcuts import render, get_list_or_404
from django.db.models import Q
from .models import Entry


def overview(request, category="Allgemein"):
    entries = Entry.objects.all().order_by('-created')
    return render(request, 'blog/list.html', {'entries': entries})


def year(request, year):
    entries = Entry.objects.filter(created__year=year).order_by('-created')
    return render(request, 'blog/list.html', {'entries': entries})


def month(request, year, month):
    entries = get_list_or_404(Entry.objects.order_by('-created'), created__year=year, created__month=month)
    return render(request, 'blog/list.html', {'entries': entries})


def day(request, year, month, day):
    entries = get_list_or_404(Entry.objects.order_by('-created'), created__year=year, created__month=month, created__day=day)
    return render(request, 'blog/list.html', {'entries': entries})


def tag(request, tag):
    try:
        entries = Entry.objects.filter(Q(tags=tag)).order_by('-created')
    except Entry.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'blog/list.html', {'entries': entries})
