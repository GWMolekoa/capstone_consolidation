from django.db import models

# Create your models here.

class Myband(models.Model):
    """
    Model representing a musical band.

    Attributes:
        name (str): The name of the band. :noindex:
        genre (str): The genre of music the band plays. :noindex:
        year_formed (int): The year the band was formed. :noindex:
        popular_songs (str): List of popular songs by the band. :noindex:
        body (str): Description or information about the band. :noindex:
    """
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    year_formed = models.IntegerField()
    popular_songs = models.CharField(max_length=250)
    body = models.TextField(default='About Artist')

    def __str__(self):
        """
        String representation of the Myband object.

        Returns:
            str: The name of the band followed by its genre.
        """
        return f"{self.name}, {self.genre}"
