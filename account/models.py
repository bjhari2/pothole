from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Corporator(models.Model):
    ward_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class User(AbstractUser):
    is_user = models.BooleanField('Is user', default=False)
    is_contractor = models.BooleanField('Is contractor', default=False)
    is_corporator = models.BooleanField('Is corporator', default=False)
    ward_no = models.ForeignKey(Corporator, on_delete=models.CASCADE, null=True, db_column='ward_no')


class Contractor(models.Model):
    c_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Pothole(models.Model):
    p_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=500)
    remarks = models.CharField(max_length=500)
    date = models.DateField()
    img = models.ImageField(upload_to='images/', default='pothole.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    ward_no = models.ForeignKey(Corporator, on_delete=models.CASCADE, db_column='ward_no')


class Allotment(models.Model):
    p_id = models.IntegerField(primary_key=True)
    c_id = models.IntegerField()




