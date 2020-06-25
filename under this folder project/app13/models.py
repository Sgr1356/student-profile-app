from django.db import models

# Create your models here.


class studentmodel(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    contact=models.IntegerField(unique=True)
    gender=models.CharField(max_length=10)
    username=models.CharField(max_length=30,unique=True,default=False)

class loginmodel(models.Model):
    username=models.CharField(unique=True,max_length=30)
    password=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
