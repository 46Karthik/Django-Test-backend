from django.db import models

# Create your models here.

class User(models.Model):
    # id = models.AutoField(db_column="ID",primary_key=True)
    name = models.CharField(max_length=100)
    
    def _str_(self):
        return name

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'