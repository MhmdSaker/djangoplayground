from django.db import models

# Create your models here.



class Animal(models.Model):
    name = models.CharField(max_length= 100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()



    
class Keeper(models.Model):
    animal = models.ForeignKey(Animal, on_delete= models.CASCADE)
    
    
    