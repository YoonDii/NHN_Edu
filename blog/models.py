from django.db import models


# Create your models here.

class Searchlist(models.Model):
    parse_type = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    published_datetime = models.DateTimeField(blank=True, null=True)
    attachment_list = models.TextField(blank=True, null=True, default="None")

    def __str__(self):
        return self.title