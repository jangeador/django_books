from bootstrap_modal_forms.forms import BSModalForm, BSModalModelForm
from crispy_forms.helper import FormHelper
from django import forms
from django_select2.forms import Select2Widget

from books.models import Book, Author


class BookForm(BSModalModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=Select2Widget)

    class Meta:
        model = Book
        fields = ["title", "author", "pages", "country", "language", "link", "year"]

    helper = FormHelper()
    helper.form_tag = False


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]
