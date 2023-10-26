from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Book
from datetime import date

# Create your tests here.
class RedirectTests(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_book_list(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, 302)
    
    def test_book_create(self):
        response = self.client.get(reverse('book-create'))
        self.assertEqual(response.status_code, 302)


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.book = Book.objects.create(
            title='A good title', 
            author='John Doe', 
            published_date=date.today(), 
            price= 19.99)

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'A good title')

    def test_book_retrieval(self):
        book_from_db = Book.objects.get(id=self.book.id)
        self.assertEqual(book_from_db, self.book)
     
    def test_book_update(self):
        self.book.title = "An updated title"
        self.book.save()
        book_from_db = Book.objects.get(id=self.book.id)
        self.assertEqual(book_from_db.title, "An updated title")
     
    def test_book_deletion(self):
        book_id = self.book.id
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)
     
    def test_str_representation(self):
        self.assertEqual(str(self.book), 'A good title')

    def test_book_get_absolute_url(self):
        expected_url = reverse('book-detail', args=[self.book.id])
        self.assertEqual(self.book.get_absolute_url(), expected_url)


from django.test import RequestFactory
from .language_middleware import LanguageMiddleware
from django.http import HttpResponse

class LanguageMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = LanguageMiddleware(lambda rec: HttpResponse('Bla'))
    
    def test_language_header_added(self):
        request = self.factory.get('/')
        response = self.middleware(request)

        self.assertEqual(response['Language'], 'en-US')