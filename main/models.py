from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255) # Title of writing
    amount = models.IntegerField()          # Number in series, 1 if One-Shot
    description = models.TextField()        # General gist of it
    word_Count = models.IntegerField()      # Word count
    genre = models.CharField(max_length=255)# Genre of writing
    character_Source = models.TextField()   # Source of characters

# class Employee(models.Model):
#    name = models.CharField()
#    age = models.IntegerField()
#    hobby = models.TextField()