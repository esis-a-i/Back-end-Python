from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from .models import *


def book(request):
    if request.method == "GET":
        return get_book_list(request)
    elif request.method == "DELETE":
        delete_book_list(request)
    else:
        return HttpResponseNotAllowed(['GET', 'DELETE'])


def delete_book_list(request):
    remove_book = request.body
    for book in Book.objects.all:
        if book == remove_book:
            Book.objects.filter(id=book.id).delete()


def get_book_list(request):
    books = [{"title": book.title, "author": book.author}
             for book in Book.objects.all()]
    return render(
        request,
        'book.html',
        context={'book_list': books},
    )


def book_id(request, book_id):
    if request.method == "GET":
        return get_book(request, book_id)
    else:
        return HttpResponseNotAllowed(['GET', 'DELETE'])


def get_book(request, book_id):
    return render(
        request,
        'book.html',
        context={'book_list': Book.objects.filter(id=book_id)},
    )


def author(request):
    if request.method == "GET":
        return
    else:
        return HttpResponseNotAllowed(['GET'])


def genre(request):
    if request.method == "GET":
        return
    else:
        return HttpResponseNotAllowed(['GET'])


def index(request):
    num_books = Book.objects.all().count
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()
    if request.method == "GET":
        return render(
            request,
            'index.html',
            context={'num_books': num_books,
                     'num_genre': num_genre, 'num_authors': num_authors},
        )
    else:
        return HttpResponseNotAllowed(['GET'])
