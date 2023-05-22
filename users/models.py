from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class previousorders(models.Model):
    item = models.CharField(max_length = 30)
    quantity = models.IntegerField()
    
class vendor_profile(models.Model):
    vendor=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    income=models.IntegerField(default = 0)
    