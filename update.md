book = Book.objects.first()
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
