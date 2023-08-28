from rest_framework import serializers

from books.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "id",
            "name",
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ("id", "title", "pages", "author",
                  "country", "language", "image_link", "year", "link")
