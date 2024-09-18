from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Book, User, BorrowRecord
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404
from .models import Book, BorrowRecord
from django.utils import timezone
# Create your views here.


# Register a new user
def enroll_user(request):
    if request.method == "POST":
        data = request.POST
        user = User.objects.create(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        return JsonResponse({'status': 'User enrolled successfully', 'user_id': user.id})

# List available books
def list_books(request):
    books = Book.objects.filter(available=True)
    return JsonResponse({'books': list(books.values())})

# Get single book by ID
def get_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return JsonResponse({'book': book.title, 'author': book.author, 'category': book.category})

# Filter books
def filter_books(request):
    publisher = request.GET.get('publisher')
    category = request.GET.get('category')
    books = Book.objects.filter(available=True)
    if publisher:
        books = books.filter(publisher=publisher)
    if category:
        books = books.filter(category=category)
    return JsonResponse({'books': list(books.values())})

# Borrow a book by ID
def borrow_book(user_id, book_id, borrow_days):
    book = get_object_or_404(Book, id=book_id)

    if not book.available:
        return {'status': 'Book not available'}

    return_date = timezone.now().date() + timedelta(days=borrow_days)

    # Create the borrow record
    BorrowRecord.objects.create(
        user_id=user_id,
        book=book,
        return_date=return_date
    )

    # Update the book availability
    book.available = False
    book.available_on = return_date
    book.save()

    return {'status': 'Book borrowed successfully'}

def return_book(borrow_record_id):
    borrow_record = get_object_or_404(BorrowRecord, id=borrow_record_id)
    book = borrow_record.book

    # Update the book availability
    book.available = True
    book.available_on = None
    book.save()

    return {'status': 'Book returned successfully'}