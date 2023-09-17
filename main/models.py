from django.db import models
from django.contrib.auth import get_user_model

class Item(models.Model):
    name = models.CharField(max_length=255) # Title of writing
    amount = models.IntegerField()          # Number in series, 1 if One-Shot
    description = models.TextField()        # General gist of it
    word_Count = models.IntegerField()      # Word count
    genre = models.CharField(max_length=255)# Genre of writing
    character_Source = models.TextField()   # Source of characters