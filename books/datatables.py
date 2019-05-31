from datatableview import Datatable
from datatableview import columns
from django.urls import reverse
from django.utils.safestring import mark_safe


class BookDatatable(Datatable):

    actions = columns.TextColumn(processor='get_actions')

    class Meta:
        columns = ['name', 'pages', 'author']
        search_fields = ['name', 'author__name']

    def get_actions(self, instance, *args, **kwargs):
        url_kwargs = {'pk': instance.pk}
        detail_url = reverse('book_view', kwargs=url_kwargs)
        edit_url = reverse('book_edit', kwargs=url_kwargs)
        delete_url = reverse('book_delete', kwargs=url_kwargs)
        template = '''
        <button type="button" class="read-book btn btn-sm btn-primary"
                data-id="{0}">
            <span class="fa fa-eye"></span>
        </button>
        <!-- Update book buttons -->
        <button type="button" class="update-book btn btn-sm btn-primary"
                data-id="{1}">
            <span class="fa fa-edit"></span>
        </button>
        <!-- Delete book buttons -->
        <button type="button" class="delete-book btn btn-sm btn-danger"
                data-id="{2}">
            <span class="fa fa-trash"></span>
        </button>
        '''
        return mark_safe(template.format(
            detail_url,
            edit_url,
            delete_url
        ))