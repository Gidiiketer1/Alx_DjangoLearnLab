from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()  # Ensure this field exists
    isbn = models.CharField(max_length=13)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    @property
    def publication_year(self):
        return self.published_date.year if self.published_date else None
