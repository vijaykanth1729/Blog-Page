from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name = 'list.html'
    ordering = ['-date']
    paginate_by = 3
    context_object_name = 'object'


class EntryDetail(LoginRequiredMixin,DetailView):
    model = Entry
    template_name = 'myapp/entry_detail.html'


class CreateEntry(LoginRequiredMixin,CreateView):
    model = Entry
    template_name = 'create_entry.html'
    fields = ['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)