from django.db import models

# Create your models here.
class Table1(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pic')
    desc = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    names = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='pic')
    details = models.TextField()

    def __str__(self):
        return self.names
