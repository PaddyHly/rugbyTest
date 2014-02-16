from django.db import models

#should the teams be completely seperated from modeling the leagues/fixtures,
#i.e. in a seperate 'app' and then imported in?
#are we tracking individual players?
class Team(models.Model):
    name = models.CharField(max_length=50)
    venue_name = models.CharField(max_length=50)
    home_pitch_location = models.CharField(max_length=50)

class League(models.Model):
    title = models.CharField(max_length=50)
    teams = models.ManyToManyField(Team)

class Fixture(models.Model):
    league_part_of = models.ForeignKey(League)
    teams = models.ManyToManyField(Team)
    venue = models.CharField(max_length=50)