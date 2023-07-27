from django.db import models

# Create your models here.
class student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField (max_length=20)
    password =models.CharField (max_length=30)
    comfirm_password =models.CharField(max_length=30)


    
    
class super_user(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField (max_length=20)
    password =models.CharField (max_length=30)
    confirm_password =models.CharField(max_length=30)

class superduper_user(models.Model):  #to upload image we have to create new model
    username = models.CharField(max_length=100)
    email = models.EmailField (max_length=20)
    password =models.CharField (max_length=30)
    confirm_password =models.CharField(max_length=30)
    photo = models.ImageField(upload_to='images/')

    