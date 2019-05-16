from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from books.forms import BookForm, AuthorForm
from books.models import Book, Author
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

class BookList(ListView):
    model = Book


class BookView(DetailView):
    model = Book


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


class AuthorList(ListView):
    model = Author


class AuthorView(BSModalReadView):
    model = Author


class AuthorCreate(BSModalCreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')


class AuthorUpdate(BSModalUpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')
