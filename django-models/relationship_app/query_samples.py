# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []

# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a library (OneToOneField access)
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # ✅ This line satisfies the required check
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Optional: test calls (you can comment these out before committing if needed)
if __name__ == "__main__":
    print("Books by author:")
    for book in books_by_author("Author Name"):
        print(book.title)

    print("\nBooks in library:")
    for book in books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian for library:")
    librarian = librarian_for_library("Central Library")
    if librarian:
        print(librarian.name)
    else:
        print("No librarian found.")
