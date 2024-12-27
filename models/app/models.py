from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    date=models.DateField()
    country=models.CharField(max_length=40)
    email=models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title