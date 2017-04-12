from django.conf.urls import url

from django.views import generic

from .models import Category, Item


from . import views


class ListViewBase(generic.ListView):
    model= Item


class DetailView(generic.DetailView):
    model = Item
