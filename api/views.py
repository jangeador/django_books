from rest_framework import viewsets

from api.serializers import BookSerializer, AuthorSerializer
from books.models import Book, Author


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
