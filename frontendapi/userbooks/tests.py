from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.test import Client
from .models import Book
from django.utils import timezone
from datetime import timedelta
from .models import BorrowRecord
# Create your tests here.


class FrontendAPITests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_enroll_user(self):
        response = self.client.post('api/enroll_user/'), {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'User enrolled successfully'})
        self.assertTrue(User.objects.filter(email='test@example.com').exists())


class FrontendAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(
            title='Book Title',
            author='Book Author',
            publisher='Book Publisher',
            category='Book Category',
            available=True
        )

    def test_list_books(self):
        response = self.client.get('api/list_books/')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('books', data)
        self.assertEqual(len(data['books']), 1)
        self.assertEqual(data['books'][0]['title'], 'Book Title')

class FrontendAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(
            title='Book Title',
            author='Book Author',
            publisher='Book Publisher',
            category='Book Category',
            available=True
        )

    def test_get_book(self):
        response = self.client.get('api/get_book/', args=[self.book.id])

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['book']['title'], 'Book Title')
        self.assertEqual(data['book']['author'], 'Book Author')

class FrontendAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.book1 = Book.objects.create(
            title='Book Title 1',
            author='Author 1',
            publisher='Wiley',
            category='Technology',
            available=True
        )
        self.book2 = Book.objects.create(
            title='Book Title 2',
            author='Author 2',
            publisher='Manning',
            category='Fiction',
            available=True
        )

    def test_filter_books(self):
        response = self.client.get('api/filter_books/' + '?publisher=Wiley&category=Technology')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('books', data)
        self.assertEqual(len(data['books']), 1)
        self.assertEqual(data['books'][0]['title'], 'Book Title 1')