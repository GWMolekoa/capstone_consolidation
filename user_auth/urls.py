"""
URL configuration for the user_auth application.

This module defines the URL patterns for the user_auth app, mapping URLs to 
views for handling user registration and other authentication-related operations.
"""

from django.urls import path
from .views import UserRegisterView

# URL patterns for the user_auth app
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # Maps the 'register/' URL to the UserRegisterView class-based view
    # Handles user registration functionality
    # The 'name' parameter allows this URL to be easily referenced in templates and views
]
