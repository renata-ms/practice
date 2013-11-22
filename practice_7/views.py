#!/usr/bin/python
# -*- coding: cp1251 -*-

from django.shortcuts import render_to_response
from library.models import Book, Author
from django.template import Context, Template

from django.views.generic import ListView
from django.views.generic import DetailView

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books.html'


class BookDetail(DetailView):
    model = Book
    context_object_name = 'book_card'
    template_name = 'book_card.html'


class AuthorList(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'authors.html'


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'author_card.html'


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/registration.html", {
        'form': form,
    })
