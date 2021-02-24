from django.db import models

# Create your models here.

class Items(models.Model):

    item = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    price = models.IntegerField()
    
    def __str__(self):
        return self.item