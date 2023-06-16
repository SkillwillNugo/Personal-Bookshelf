from django.urls import path
from .views import (BookListView, BookDetailView, BookCreateView,
                    BookUpdateView, BookDeleteView, AuthorListView,
                    AuthorDetailView, AuthorCreateView, AuthorUpdateView,
                    AuthorDeleteView)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/new/', BookCreateView.as_view(), name='book_new'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),

    path('author/', AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/new/', AuthorCreateView.as_view(), name='author_new'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
]
