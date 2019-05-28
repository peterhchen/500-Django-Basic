from django.urls import path
from django.conf.urls import url
from . import views

# '$' means end of string. put nothing here.
urlpatterns = [
    # /music/ : 
    # the following does not match any pattern and just go to home page.
    # no extra information on it. ^: Beginning, $: end
    url(r'^$', views.index, name='index'),
    # /music/712/some id=71 of music
    # (): Group, signify one item. ?P<parameter-name>[0-9]+
    # There is a "/" at the end of string. It treats as a ID of the group.
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # The following line does not work
    #path(r'^$', views.index, name='index'),
]