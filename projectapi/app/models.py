from django.db import models

# Create your models here.
class student(models.Model):
    roll_no=models.IntegerField()
    age=models.CharField()
    age=models.IntegerField()
    email=models.EmailField()

