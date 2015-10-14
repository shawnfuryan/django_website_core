from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about.*$', views.about, name='about'),
    url(r'^contact.*$', views.contact, name='contact'),
    url(r'^404.*$', views.handler404, name='404'),
    url(r'^50.*$', views.handler500, name='500'),
]
