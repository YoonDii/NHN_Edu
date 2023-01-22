from django.db import models

# Create your models here.

class Searchlist(models.Model):
    url = models.CharField(max_length=500)
    title = models.CharField(max_length = 200)
    published_datetime = models.DateTimeField(auto_now_add = True)
    boby = models.CharField(max_length=500)
    attachment_list = models.CharField(max_length=500)

