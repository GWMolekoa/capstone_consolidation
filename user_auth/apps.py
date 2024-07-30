"""
Module for configuring the user_auth application.

This module contains the application configuration class for the user_auth
application, which sets the default auto field and the application name.
"""

from django.apps import AppConfig

class UserAuthConfig(AppConfig):
    """
    Configuration for the user_auth application.

    This class is used to configure the user_auth application,
    specifying the default auto field and the application name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'
