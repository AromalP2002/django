from django.db import models


# Create your models here.
class movie(models.Model):
    name=models.TextField()
    date=models.DateField()
    frgrnd_img=models.FieldFile()
    bckgrd_img=models.FieldFile()
    lang=models.TextField()
    durtn=models.TextField()
    diamtn=models.TextField()
