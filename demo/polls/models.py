from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 255)
    birthday = models.DateField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length= 255)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    year = models.IntegerField()
    
    def __str__(self):
        return self.name
