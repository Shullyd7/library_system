from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Book, User
from .rabbitmq import get_rabbitmq_connection

# Create your views here.


def notify_frontend(book, action):
    channel = get_rabbitmq_connection()
    message = {
        'action': action,
        'book_id': book.id,
        'title': book.title,
        'author': book.author,
        'publisher': book.publisher,
        'category': book.category
    }
    channel.basic_publish(exchange='',
                          routing_key='book_updates',
                          body=json.dumps(message))
    channel.connection.close()

# Add a new book
def add_book(request):
    if request.method == "POST":
        data = request.POST
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            publisher=data['publisher'],
            category=data['category'],
        )
        notify_frontend(book, 'add')
        return JsonResponse({'status': 'Book added successfully', 'book_id': book.id})

# Remove a book
def remove_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    notify_frontend(book, 'remove')
    return JsonResponse({'status': 'Book removed successfully'})

# Fetch all users
def list_users(request):
    users = User.objects.all()
    return JsonResponse({'users': list(users.values())})

# Fetch borrowed books
def list_borrowed_books(request):
    borrowed_books = Book.objects.filter(available=False)
    return JsonResponse({'borrowed_books': list(borrowed_books.values())})