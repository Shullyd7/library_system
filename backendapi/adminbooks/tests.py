from django.test import TestCase, Client
from unittest.mock import patch
from .models import User, Book

# Create your tests here.


class BackendAPITests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('backendapi.adminbooks.views.notify_frontend')  # Mock RabbitMQ notification
    def test_add_book(self, mock_notify):
        response = self.client.post('api/add_book/'), {
            'title': 'New Book',
            'author': 'New Author',
            'publisher': 'New Publisher',
            'category': 'New Category',
        }

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'Book added successfully'})
        self.assertTrue(Book.objects.filter(title='New Book').exists())
        mock_notify.assert_called_once()

class BackendAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(
            title='Book to Remove',
            author='Author',
            publisher='Publisher',
            category='Category'
        )

    @patch('backendapi.adminbooks.views.notify_frontend')  # Mock RabbitMQ notification
    def test_remove_book(self, mock_notify):
        response = self.client.delete('api/remove_book', args=[self.book.id])

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'Book removed successfully'})
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
        mock_notify.assert_called_once()

class BackendAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email='user1@example.com', first_name='John', last_name='Doe')

    def test_list_users(self):
        response = self.client.get('api/list_users/')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('users', data)
        self.assertEqual(len(data['users']), 1)
        self.assertEqual(data['users'][0]['email'], 'user1@example.com')

class BackendAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email='user@example.com', first_name='John', last_name='Doe')
        self.book = Book.objects.create(
            title='Book Title',
            author='Book Author',
            publisher='Book Publisher',
            category='Book Category',
            available=False
        )

    def test_list_borrowed_books(self):
        response = self.client.get('api/list_borrowed_books/')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('borrowed_books', data)
        self.assertEqual(len(data['borrowed_books']), 1)
        self.assertEqual(data['borrowed_books'][0]['title'], 'Book Title')