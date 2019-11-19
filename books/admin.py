from django.contrib import admin
from books.models import Book, Author
from import_export.admin import ImportExportActionModelAdmin

from books.resources import BookResource


class BookAdmin(ImportExportActionModelAdmin):
	resource_class = BookResource


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
