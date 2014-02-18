from django.db import models

class Club(models.Model):
    president = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class Team(models.Model):
    club = models.ForeignKey(Club)
    currentLeague = models.ForeignKey('league.models.League')
    leaguePoints = models.PositiveIntegerFiled()

class Player(models.Model):
	name = models.CharField(max_length=50)
	team = models.ForeignKey(Team)
    dob = models.DateField()
    jerseyNum = models.PositiveIntegerFiled()