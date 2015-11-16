from django.shortcuts import get_object_or_404, render
from django.http import Http404


def index(request):
#    try:
#        posts = Entry.objects.all()[:3]
#        print(posts)
#    except Entry.DoesNotExist:
#        raise Http404("Keine Beiträge vorhanden.")
    return render(request, 'index.html')