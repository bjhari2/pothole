from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)
    is_contractor = models.BooleanField('Is contractor', default=False)
    is_corporator = models.BooleanField('Is corporator', default=False)
    is_section_officer = models.BooleanField('Is section officer', default=False)


class Pothole(models.Model):
    p_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=500)
    remarks = models.CharField(max_length=500)
    date = models.DateField()
    img = models.ImageField(upload_to='images/', default='pothole.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1000')
    




