from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import *


def book(request):
    if request.method == "GET":
        return JsonResponse({
            "description": "Page with list of book",
            "list of book": [
                {"Name": "Harry Potter",
                 "Author": "JK. Rowling",
                 "ISBN": "12345678",
                 "Genre": "Fantasy", }
            ],
        })
    elif request.method == "POST":
        return JsonResponse({
            "Book": {"Name": "Harry Potter",
                     "Author": "JK. Rowling",
                     "ISBN": "12345678",
                     "Genre": "Fantasy", }
        })
    else:
        return HttpResponseNotAllowed(request.method)


def author(request):
    if request.method == "GET":
        return JsonResponse({
            "description": "Page with list of author",
            "list of author":
            [{"Author name": "name"}],
        })
    else:
        return HttpResponseNotAllowed(request.method)


def genre(request):
    if request.method == "GET":
        return JsonResponse({
            "description": "Page with list of genre",
            "list of genre":
            [{"Genre": "genre"}],
        })
    else:
        return HttpResponseNotAllowed(request.method)


def index(request):
    # num_books = Book.objects.all().count
    # num_authors = Author.objects.count()
    # num_genre = Genre.objects.count()
    if request.method == "GET":
        return render(
            request,
            'index.html',
            context={'num_books': "15", 'num_authors': "11", 'num_genre': "3"},
        )
    else:
        return HttpResponseNotAllowed(request.method)
