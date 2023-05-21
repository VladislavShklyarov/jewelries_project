from django.db import models

class Reply(models.Model):
    name =  models.CharField('Имя', max_length=30)
    email = models.EmailField('email')
    text = models.TextField('Что понравилось / не понравислось?')

    def __str__(self):
        return self.text