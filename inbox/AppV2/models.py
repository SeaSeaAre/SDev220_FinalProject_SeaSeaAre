from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    ssn = models.CharField(max_length=9)
    # You may add additional fields here like files, notes, encounters if you want to store them in the database.

    def __str__(self):
        return self.name