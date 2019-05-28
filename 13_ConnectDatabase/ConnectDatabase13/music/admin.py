from django.contrib import admin

# from models we import the class Album
from .models import Album
# The class Album should have admin interface.
admin.site.register (Album)