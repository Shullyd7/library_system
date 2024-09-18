from django.urls import path
from . import views

urlpatterns = [
    # Add a new book
    path('add_book/', views.add_book, name='add_book'),

    # Remove a book
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),

    # Fetch all users
    path('list_users/', views.list_users, name='list_users'),

    # Fetch borrowed books
    path('list_borrowed_books/', views.list_borrowed_books, name='list_borrowed_books'),
]