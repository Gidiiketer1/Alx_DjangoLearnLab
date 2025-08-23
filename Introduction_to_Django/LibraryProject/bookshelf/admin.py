from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'pages')  # removed published_date
    search_fields = ('title', 'author', 'isbn')
    # list_filter = ('published_date',)  # comment or remove this line
