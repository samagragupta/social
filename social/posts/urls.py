from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^create$', views.create_form, name='form'),
  url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
]
