from django.db import models

# Create your models here.
class Notice(models.Model):
    notice=models.CharField(max_length=200)
    pub_date=models.DateTimeField()