from django.db import models

# Create your models here.
class My_User(models.Model):
    First_Name = models.CharField(max_length=200,)
    Last_Name = models.CharField(max_length=200,)
    Email = models.EmailField(max_length=264,unique=True)

    def __str__(self):
        return self.First_Name

