from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # 📚 Book and Library views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # 👤 User authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # 🔐 Role-based access views
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),
]
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

]
# Added book management URLs with permissions
path('books/add/', views.add_book, name='add_book'),
path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
