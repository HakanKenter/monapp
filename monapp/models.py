from django.db import models

# Create your models here.

class City(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Interest(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    interest = models.ManyToManyField(Interest)
    
    def __str__(self):
        return self.first_name
    
class PersonAddress(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    street_number = models.CharField(max_length=200)
    
    def __str__(self):
        return self.street_number + " | " + self.person.first_name + " | " + self.city.title