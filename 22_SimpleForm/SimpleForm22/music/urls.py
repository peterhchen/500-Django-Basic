from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'music'
# '$' means end of string. put nothing here.
urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # this favorite page is for user click and save. Refresh for default page with click.
    # /music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
]