from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
#    try:
#        posts = Entry.objects.all()[:3]
#        print(posts)
#    except Entry.DoesNotExist:
#        raise Http404("Keine Beiträge vorhanden.")
    return render(request, 'index.html')