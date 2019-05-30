from django.contrib import admin
from .models import Album, Song
# The class Album should have admin interface.
admin.site.register (Album)
admin.site.register (Song)