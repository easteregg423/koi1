from django.db import models

# Create your models here.

class Data(models.Model):
    file_name=models.FilePathField()
    pub_date=models.DateTimeField()