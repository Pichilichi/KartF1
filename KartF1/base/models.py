from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Kart(models.Model):
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body[0:50]

#     class Meta:
#         ordering = ['-updated']

# class User(models.Model):  
#     name = models.CharField(max_length=255)
#     photo = models.ImageField(upload_to="cars") 
# email = campo del email por si se puede hacer uno en plan “te has registrado!”	
# cosa que debería estar en el proyecto del mac btw

class Kart(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="static/images/cars") 
    cc = models.IntegerField()
    color = models.CharField(max_length=255)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
          return self.name
     
class Circuit(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="static/images/circuits") 
    year = models.DateField()
    km = models.CharField(max_length=255)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
            return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="static/images/equipment") 
    HELMET = "HM"
    RACESUIT = "RS"
    GLOVES = "GL"
    EQUIPMENT_CHOICES = [
        (HELMET, "Helmet"),
       	(RACESUIT, "RaceSuit"),
        (GLOVES, "Gloves"), 
    ]
    equipment_category = models.CharField(
       	max_length=2,
        choices=EQUIPMENT_CHOICES,
        default=HELMET,
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name

# class Ranking(models.Model):
	
class Booking(models.Model): 
    name = models.CharField(max_length=255) 
    raceDay = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    racers = models.ManyToManyField(User, related_name='racers', blank=True)
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
            return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.body[0:50]
    
    class Meta:
        ordering = ['-updated', '-created']

class Weather(models.Model):
    name = models.CharField(max_length=255) 
    photo = models.ImageField(upload_to="static/images/forecast") 
    tempMin = models.IntegerField()
    tempMax = models.IntegerField()
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
            return self.name
