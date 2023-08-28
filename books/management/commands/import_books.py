import json

from django.core.management.base import BaseCommand, CommandError

from books.models import Author, Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("books/static/data/books.json", "r") as json_file:
            data = json.load(json_file)

            for book in data:

                author, created = Author.objects.get_or_create(name=book["author"])

                book, created = Book.objects.get_or_create(
                    title=book["title"],
                    defaults={
                        "author": author,
                        "pages": book["pages"],
                        "country": book["country"],
                        "language": book["language"],
                        "link": book["link"],
                        "year": book["year"],
                        "image_link": book["imageLink"],
                    },
                )

                print(book)