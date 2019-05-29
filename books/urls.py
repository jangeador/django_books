from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('list2', views.BookDatatableView.as_view(), name='book_list2'),
    path('new', views.BookCreate.as_view(), name='book_new'),
    path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
    path('edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
    path('authors', views.AuthorList.as_view(), name='author_list'),
    path('new_author', views.AuthorCreate.as_view(), name='author_new'),
    path('view_author/<int:pk>', views.AuthorView.as_view(), name='author_view'),
    path('edit_author/<int:pk>', views.AuthorUpdate.as_view(), name='author_edit'),
    path('delete_author/<int:pk>', views.AuthorDelete.as_view(), name='author_delete'),
]