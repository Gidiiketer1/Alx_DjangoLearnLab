from bookshelf.models import Book

# Create a new book
book = Book(title="Django for Beginners", author="William S. Vincent", isbn="1234567890123")
book.save()

# Confirm creation
print(book)
