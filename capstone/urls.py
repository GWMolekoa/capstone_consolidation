from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URLs
    path('', include('myband.urls')),  # Include URLs from the 'myband' app
    path('user_auth/', include('django.contrib.auth.urls')),  # Django's built-in authentication URLs
    path('user_auth/', include('user_auth.urls')),  
]