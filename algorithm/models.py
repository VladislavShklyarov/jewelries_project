from django.db import models

class Algorithm(models.Model):
    D = models.CharField(max_length=20)
    A = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
