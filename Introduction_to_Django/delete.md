# Delete a book
book = Book.objects.get(id=1)
book.delete()

# Confirm deletion
print(Book.objects.all())
