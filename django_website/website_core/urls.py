from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^404.*$', views.handler404, name='404'),
    url(r'^50.*$', views.handler500, name='500'),
]
