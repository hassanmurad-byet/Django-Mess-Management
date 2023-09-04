from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    name =models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    phone = models.IntegerField()
    profil_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.name
    
class Meal(models.Model):
    Name=models.ForeignKey(Member,on_delete=models.CASCADE)
    MealDate =models.DateField()
    Deposite =models.IntegerField()

    meals = models.FloatField()

    def __int__(self):
        return self.Deposite


class UserInfo(models.Model):

    username = models.OneToOneField(User,on_delete=models.CASCADE)
    
 

    def __str__(self):
        return self.user.username





