
from django.db import models

# Create your models here.

class Detail(models.Model):

    name = models.CharField(max_length=255)
    roll_number = models.IntegerField()
    class_standard = models.IntegerField()


    def __str__(self):
        return self.name



class Parent_Detail(models.Model):

    parent_name = models.CharField(max_length=255)
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)


    def __str__(self):
        return self.parent_name
