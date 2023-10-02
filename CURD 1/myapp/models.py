from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    eddress=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.name
