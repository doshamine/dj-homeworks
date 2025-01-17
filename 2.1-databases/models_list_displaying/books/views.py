import re
from datetime import datetime

from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = list(Book.objects.values())
    context = {"books": books}
    return render(request, template, context)

def books_by_date_view(request, pub_date):
    template = 'books/books_by_date_list.html'
    books = list(Book.objects.values())
    pub_date = pub_date.strftime('%Y-%m-%d')
    books_by_date = list(filter(lambda book: book["pub_date"].strftime('%Y-%m-%d')==pub_date, books))
    prev_object = Book.objects.values().filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    next_object = Book.objects.values().filter(pub_date__gt=pub_date).order_by('pub_date').first()

    prev_page = ""
    next_page = ""

    if prev_object:
        prev_page = prev_object.get("pub_date").strftime('%Y-%m-%d')

    if next_object:
        next_page = next_object.get("pub_date").strftime('%Y-%m-%d')

    context = {
        "books": books_by_date,
        "prev_page": prev_page,
        "next_page": next_page
    }
    return render(request, template, context)
