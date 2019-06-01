#from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album

def index (request):
    all_albums = Album.objects.all()
    #context = {'all_albums': all_albums }
    #return HttpResponse(template.render(context, request))
    return render (request, 'music/index.html', {'all_albums': all_albums })

def detail(request, album_id):
    # we want to check the database and check the album is there or not.
    #return HttpResponse ("<h2>details for Album id: " + str (album_id) + "</h2>")
    # try:
    #     album = Album.objects.get (pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404 ("Album does not exist")
    # return render (request, 'music/detail.html', {'album': album })
    album = get_object_or_404 (Album, pk=album_id)
    return render (request, 'msuic/detail.html', {'alnum': album })

def favorite(request, album_id):
    # we want to check the database and check the album is there or not.
    #return HttpResponse ("<h2>details for Album id: " + str (album_id) + "</h2>")
    # try:
    #     album = Album.objects.get (pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404 ("Album does not exist")
    # return render (request, 'music/detail.html', {'album': album })
    album = get_object_or_404 (Album, pk=album_id)
    return render (request, 'msuic/detail.html', {'alnum': album })