from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Homepage showing all posts
    path('', views.post_list, name='post_list'),

    # Blog post CRUD
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # User Authentication
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]