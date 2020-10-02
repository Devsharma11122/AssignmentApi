from django.db import models

# Create your models here.
class Products(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    RAM = models.IntegerField()
    Processor = models.CharField(max_length=50)
    TYPE =(
        ('M','Mobile'),
        ('L','Laptop'),
    )
    Type = models.CharField(max_length=10, choices= TYPE)


    def __str__(self):
        return self.Name