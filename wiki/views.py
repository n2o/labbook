from django.shortcuts import render, get_list_or_404
from .models import Item


def list(request):
    items = get_list_or_404(Item)
    return render(request, 'wiki/list.html', {'items': items})