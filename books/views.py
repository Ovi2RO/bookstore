from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Book
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_date', 'price']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_date', 'price']
    template_name = 'books/book_edit.html'

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.object.pk})

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book-list')

