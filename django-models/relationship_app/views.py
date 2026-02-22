from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Library
from .models import Book


# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: Detail view for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()
        return context


# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})
