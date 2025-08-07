book = Book.objects.first()
book.delete()
print(Book.objects.all())
