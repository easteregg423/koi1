from django.db import models

# Create your models here.

class Gallary(models.Model):
    imgNm =models.ImageField(upload_to='%Y/%m/%d')
    description = models.TextField(max_length=500, blank=True)
    pub_date=models.DateTimeField(auto_now=True)