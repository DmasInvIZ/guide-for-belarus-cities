from django.views.generic import ListView
from django.shortcuts import render

from guide.models import News


class ListObjectsView(ListView):
    model = News
    template_name = 'base.html'
    context_object_name = 'news'


def about_view(request):
    return render(request, 'about.html')


def what_to_watch_view(request):
    return render(request, 'what-to-watch.html')
