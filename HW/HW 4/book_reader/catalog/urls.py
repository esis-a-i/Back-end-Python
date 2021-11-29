from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', index, name='index'),
    path('author/', author, name='author'),
    path('genre/', genre, name='genre'),
    path('book/', book, name='book'),
]
