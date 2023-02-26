from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    author = models.CharField(max_length= 120, default="Redima Kashyap")