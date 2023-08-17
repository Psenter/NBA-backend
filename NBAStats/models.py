from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.username
    
class Players(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    jersey_number = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200)
    weight = models.FloatField()
    height = models.CharField(max_length=200)
    ppg = models.FloatField()
    apg = models.FloatField()
    rpg = models.FloatField()
    spg = models.FloatField()
    bpg = models.FloatField()
    field_goal_percent = models.FloatField()
    three_pointer_percent = models.FloatField()
    free_throw_percent = models.FloatField()
    turnovers = models.FloatField()
    minutes_played = models.FloatField()
    #media_id = models.ForeignKey('Media', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teams(models.Model):
    team_name = models.CharField(max_length=200)
    wins = models.IntegerField()
    losses = models.IntegerField()
    conference_id = models.ForeignKey('conference', on_delete=models.PROTECT, null=True)
    #media_id = models.ForeignKey('Media', on_delete=models.PROTECT, null=True)
    players = models.ManyToManyField('Players')

    def __str__(self):
        return self.title

class Conference(models.Model):
    conference_location = models.CharField(max_length=200)

    def __str__(self):
        return self.conference_location
    
class Media(models.Model):
    type = models.CharField(max_length=200)
    asset_url = models.URLField()

    def __str__(self):
        return self.title