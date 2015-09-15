from django.db import models

# Create your models here.
class Qna(models.Model):
    que = models.CharField(max_length=200)
    pub_date = models.DateTimeField()