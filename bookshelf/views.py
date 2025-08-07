from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book

# CREATE
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        published_date = request.POST['published_date']
        Book.objects.create(
            title=title,
            author=author,
            description=description,
            published_date=published_date
        )
        return HttpResponse("Book created successfully.")
    return render(request, 'bookshelf/create_book.html')

# READ
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# UPDATE
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST['description']
        book.published_date = request.POST['published_date']
        book.save()
        return HttpResponse("Book updated successfully.")
    return render(request, 'bookshelf/update_book.html', {'book': book})

# DELETE
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse("Book deleted successfully.")
