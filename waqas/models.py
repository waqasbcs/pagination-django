from django.db import models

# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    published_date = models.DateField()
    
