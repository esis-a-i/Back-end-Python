from django.contrib import admin
from catalog.models import *


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    list_filter = ('first_name',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
