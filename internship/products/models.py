from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    created_at=models.CharField(max_length=100)
    updated_at=models.CharField(max_length=100)