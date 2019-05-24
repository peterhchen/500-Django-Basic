from django.urls import path
from django.conf.urls import url
from . import views

# '$' means end of string. put nothing here.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # The following line does not work
    #path(r'^$', views.index, name='index'),
]