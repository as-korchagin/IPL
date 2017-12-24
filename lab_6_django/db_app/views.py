from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    books = Book.objects.order_by('-name')
    genres = Genre.objects.order_by('-name')
    authors = Author.objects.order_by('-name')
    return render(request, 'index.html', {'base_books': books,
                                          'books': books,
                                          'genres': genres,
                                          'authors': authors})


def book_detail(request, id):
    books = Book.objects.order_by('-name')
    book = Book.objects.get(pk=id)
    return render(request, 'book.html', {'base_books': books,
                                         'element': book,
                                         'authors': book.author.all(),
                                         'genres': book.genre.all()})


def author_detail(request, id):
    books = Book.objects.order_by('-name')
    author = Author.objects.get(pk=id)
    return render(request, 'author.html', {'base_books': books,
                                           'element': author,
                                           'books': author.book_set.all()})


def genre_detail(request, id):
    books = Book.objects.order_by('-name')
    genre = Genre.objects.get(pk=id)
    return render(request, 'genre.html', {'base_books': books,
                                          'element': genre,
                                          'books': genre.book_set.all()})
