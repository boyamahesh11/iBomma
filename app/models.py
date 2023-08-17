from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    profile_pic=models.ImageField()
    