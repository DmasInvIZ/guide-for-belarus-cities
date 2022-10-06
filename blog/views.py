from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from django.shortcuts import render


class AboutView(CreateView):
    model = About
    template_name = 'about.html'
    context_object_name = 'posts'
    ordering = '-date'