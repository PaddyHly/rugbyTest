from django.db import models

class League(models.Model):
    title = models.CharField(max_length=50)

class Fixture(models.Model):
    home_team = models.ForeignKey(Team)
    away_team = models.ForeignKey(Team)
    venue = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=50)
    home_pitch = models.CharField(max_length=50)