from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'fecha_nacimiento')
    search_fields = ('nombre','pais')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'isbn', 'autor' ,'fecha_publicacion')
    search_fields = ('titulo','isbn')
    list_filter = ('autor',)