from django.db import models

# Create your models here.

class Myband(models.Model):
    """
    Model representing a musical band.

    Attributes:
        name (str): The name of the band.
        genre (str): The genre of music the band plays.
        year_formed (int): The year the band was formed.
        popular_songs (str): List of popular songs by the band.
        body (str): Description or information about the band.
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
