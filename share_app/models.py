from django.db import models

class ShareModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)