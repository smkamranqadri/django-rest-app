from django.db import models

class Event(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
