from django.urls import path
from . import views

urlpatterns = [
    # Register a new user
    path('enroll_user/', views.enroll_user, name='enroll_user'),

    # List available books
    path('list_books/', views.list_books, name='list_books'),

    # Get single book by ID
    path('get_book/<int:book_id>/', views.get_book, name='get_book'),

    # Filter books by publisher and category
    path('filter_books/', views.filter_books, name='filter_books'),

    # Borrow a book by ID
    path('borrow_book/', views.borrow_book, name='borrow_book'),

    # Return a book by borrow record ID
    path('return_book/', views.return_book, name='return_book'),
]