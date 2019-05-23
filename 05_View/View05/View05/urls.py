
from django.urls import include, path
from django.contrib import admin
#from django.conf.urls import include, url

urlpatterns = [
    # you can only type "localhost:8080/music" or "localhost:8080/admin"
    #url(r'^$/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
]
