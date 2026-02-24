from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),                  # Homepage showing all posts
    path('posts/<int:pk>/', views.post_detail, name='post_detail'), # View a single post
    path('posts/new/', views.post_create, name='post_create'),    # Create new post
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'), # Edit post
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'), # Delete post
    path('register/', views.register, name='register'),          # User registration
]