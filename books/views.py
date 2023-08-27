from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
)
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datatableview.views import DatatableView
from .datatables import BookDatatable
from books.forms import BookForm, AuthorForm
from books.models import Book, Author
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView,
)


class BookList(ListView):
    model = Book


class BookDatatableView(DatatableView):
    model = Book
    datatable_class = BookDatatable
    template_name = "books/datatable.html"


class BookView(BSModalReadView):
    model = Book


class BookCreate(BSModalCreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("book_list")


class BookUpdate(BSModalUpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("book_list")


class BookDelete(BSModalDeleteView):
    model = Book
    success_url = reverse_lazy("book_list")
    success_message = "Book successfully deleted"


class AuthorList(ListView):
    model = Author


class AuthorView(DetailView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("author_list")


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("author_list")


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy("author_list")
