from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Section

from . import views

app_name = 'calculate'
urlpatterns = [

    url(r'^$', views.index, name='index'),

    # ex /calcualte/add
    url(r'^add/$', views.add, name='add'),

    # ex: /calculate/details/5
    url(r'^details/(?P<section_id>[0-9]+)/$', views.detail, name='detail'),
]
