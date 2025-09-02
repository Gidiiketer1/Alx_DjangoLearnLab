from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Author One')
        self.book1 = Book.objects.create(title='Book A', publication_year=2021, author=self.author)
        self.book2 = Book.objects.create(title='Book B', publication_year=2023, author=self.author)

    def authenticate(self):
        self.client.login(username='testuser', password='testpass')

    def test_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book A')

    def test_create_book_unauthenticated(self):
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.authenticate()
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        self.authenticate()
        data = {
            "title": "Updated Title",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.put(reverse('book-update', args=[self.book1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        self.authenticate()
        response = self.client.delete(reverse('book-delete', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_year(self):
        response = self.client.get(reverse('book-list'), {'publication_year': 2023})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book B')

    def test_order_books_by_title(self):
        response = self.client.get(reverse('book-list'), {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ['Book A', 'Book B'])

    def test_search_books_by_title(self):
        response = self.client.get(reverse('book-list'), {'search': 'Book A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book A')
