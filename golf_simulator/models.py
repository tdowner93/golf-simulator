from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Club(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    distance = models.IntegerField()

class Shot(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    distance = models.IntegerField()
    weather = models.CharField(max_length=50)
    wind_speed = models.IntegerField()
    terrain = models.CharField(max_length=50)