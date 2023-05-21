from django.db import models

class Gemstone(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='gemstones/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name