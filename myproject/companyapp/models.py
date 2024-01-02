from django.db import models

# Create your models here.
class Companydb(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location= models.CharField(max_length=100)
