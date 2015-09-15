from django.db import models

# Create your models here.

class Myjob(models.Model):
    myjob = models.CharField(max_length=200)
    pub_date=models.DateTimeField()