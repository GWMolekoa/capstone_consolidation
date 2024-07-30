from django.apps import AppConfig

class MybandConfig(AppConfig):
    """
    Configuration for the Myband application.

    This class is used to configure the Myband application, specifying 
    the default auto field and the application name.

    Attributes:
        default_auto_field (str): The default field type to use for auto-generated fields.
        name (str): The name of the application, which is used to reference it within Django.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myband'
