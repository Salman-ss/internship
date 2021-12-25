from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    username=models.CharField(max_length=100)

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=100)
    created_at=models.CharField(max_length=100)
    updated_at=models.CharField(max_length=100)
