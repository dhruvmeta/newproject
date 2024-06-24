from django.db import models

# Create your models here.

class booking(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    date_time= models.DateTimeField()
    people= models.IntegerField()
    specialnote=models.CharField(max_length=30)