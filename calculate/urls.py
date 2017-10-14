from django.conf.urls import url

from . import views

app_name = 'calculate'
urlpatterns = [
    # ex: /calculate/details/5
    url(r'^details/(?P<section_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
