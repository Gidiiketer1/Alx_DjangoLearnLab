# Get all books
all_books = Book.objects.all()
print(all_books)

# Get a single book by ID
book = Book.objects.get(id=1)
print(book.title, book.author)
