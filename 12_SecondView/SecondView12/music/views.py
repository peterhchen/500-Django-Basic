#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index (request):
    return HttpResponse("<h1>This is the Music app Hoemepage </h1>")

def detail(reques, album_id):
    return HttpResponse ("<h2>details for Album id: " + str (album_id) + "</h2>")