# CRUD Operations with Django ORM

---

## ✅ Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

1984 by George Orwell (1949)

book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

Title: 1984, Author: George Orwell, Year: 1949

book.title = "Nineteen Eighty-Four"
book.save()
print(book)
Nineteen Eighty-Four by George Orwell (1949)

book.delete()
print(Book.objects.all())
<QuerySet []>



---

### ✅ Final Directory Structure (For Submission)

Your `Introduction_to_Django` folder should now include:

