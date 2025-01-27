# Generated by Django 3.2 on 2024-09-18 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
                ('available_on', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_on', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminbooks.book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('books_borrowed', models.ManyToManyField(through='adminbooks.BorrowRecord', to='adminbooks.Book')),
            ],
        ),
        migrations.AddField(
            model_name='borrowrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminbooks.user'),
        ),
    ]
