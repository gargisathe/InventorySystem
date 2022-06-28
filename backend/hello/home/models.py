from datetime import datetime
import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patients(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    uid = models.CharField(primary_key=True,max_length=30)
    name = models.CharField(max_length=30)
    father = models.CharField(max_length=30)
    mother = models.CharField(max_length=30)
    arrivalDate = models.DateTimeField(auto_now_add = True,null=True)
    def __str__(self):
        return self.uid

class PatientsRation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    name = models.CharField(max_length=20)
    uid = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True,null=True)
    def __str__(self):
        return self.uid + '_' + self.date

class Kit(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    # kit_id = models.IntegerField(primary_key=True)
    no = models.IntegerField()
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
