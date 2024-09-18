import pika
import json
from .models import Book
from .rabbitmq import get_rabbitmq_connection

def callback(ch, method, properties, body):
    message = json.loads(body)
    action = message.get('action')
    book_id = message.get('book_id')

    if action == 'add':
        Book.objects.update_or_create(
            id=book_id,
            defaults={
                'title': message.get('title'),
                'author': message.get('author'),
                'publisher': message.get('publisher'),
                'category': message.get('category'),
                'available': True
            }
        )
    elif action == 'remove':
        Book.objects.filter(id=book_id).delete()

def start_consuming():
    channel = get_rabbitmq_connection()
    channel.basic_consume(queue='book_updates', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages...')
    channel.start_consuming()
