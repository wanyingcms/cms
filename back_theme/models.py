from django.db import models

class ip(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)