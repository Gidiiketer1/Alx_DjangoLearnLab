# Update the title of the book
book = Book.objects.get(id=1)
book.title = "Django for Pros"
book.save()

# Confirm update
print(book)
