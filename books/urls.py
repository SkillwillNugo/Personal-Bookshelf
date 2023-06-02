from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),

    path('author/', views.author_list, name='author_list'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/new/', views.author_new, name='author_new'),
    path('author/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),
]
