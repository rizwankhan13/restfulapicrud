from django.db import models

# Create your models here.

class Employee(models.Model):
    username = models.CharField(max_length=30,default="user1")
    email = models.EmailField(default="a@gmail.com")
    password = models.CharField(max_length=15,default='1234')

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE
