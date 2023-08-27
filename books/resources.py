from import_export import fields, widgets
from import_export import resources

from books.models import Book, Author


class BookResource(resources.ModelResource):
    author = fields.Field(
        column_name="author",
        attribute="author",
        widget=widgets.ForeignKeyWidget(Author, field="name"),
    )

    # # Only import new items. Do not update any record
    # def skip_row(self, instance, original):
    # 	if not original.id:
    # 		return False
    # 	return True

    class Meta:
        model = Book
        fields = ("id", "name", "pages", "author")
        export_order = fields
        import_id_fields = ("id",)
