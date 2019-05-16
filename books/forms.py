from django import forms

from books.models import Book, Author
from bootstrap_modal_forms.forms import BSModalForm


class BookForm(BSModalForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'pages']

class AuthorForm(BSModalForm):
    class Meta:
        model = Author
        fields = ['name']