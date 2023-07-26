from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Login(models.Model):

    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    nickname= models.CharField(max_length=50)
    email= models.CharField(max_length=50)


def __str__(self):
    return self.firstname


class Home(models.Model):
     HomeId= models.AutoField(primary_key=True)
     HomeName= models.CharField(max_length=50)
     HomeCat= models.CharField(max_length=30)
     HomePrice= models.IntegerField()
     HomeImage=models.ImageField(upload_to="images/")


def __str__(self):
    return self.HomeName


class Like(models.Model):
    count= models.IntegerField()
    homename= models.CharField(max_length=50)
def __str__(self):
    return self.count
