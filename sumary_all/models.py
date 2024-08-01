from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Location"

class Participant(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email
    

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='location')
    participant = models.ManyToManyField(Participant,blank=True)
