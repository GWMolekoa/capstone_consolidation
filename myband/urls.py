from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bands/', views.band_list, name='band_list'),
]

"""
URL configuration for the 'myband' Django app.

This module defines URL patterns to map specific URLs to corresponding views
in the 'myband' app.

URL Patterns:
- '' (home): Maps to the 'home' view which displays the home page.
- 'bands/' (band_list): Maps to the 'band_list' view which lists bands.

Explanation:
- The empty string ('') URL pattern is mapped to the `home` view, rendering the homepage of the 'myband' application.
- The 'bands/' URL pattern is mapped to the `band_list` view, which is responsible for displaying a list of bands.
"""
