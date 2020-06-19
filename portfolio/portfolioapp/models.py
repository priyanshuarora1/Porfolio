from django.db import models

# Create your models here.
class projects(models.Model):
    name=models.CharField(max_length=50)
    detail= models.TextField()
    image=models.ImageField(upload_to='media')
    link=models.CharField(max_length=500,default='#')
    # username=models.CharField(max_length=30, unique=Fa)
class cert(models.Model):
    cert_name=models.CharField(max_length=50)
    cert_detail= models.TextField()
    cert_image=models.ImageField(upload_to='media')
    cert_link=models.CharField(max_length=500,default='#')
