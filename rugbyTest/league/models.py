from django.db import models

class League(models.Model):
    title = models.CharField(max_length=50)
    teams = models.ManyToManyField('Club.models.Team')

class Fixture(models.Model):
    league_part_of = models.ForeignKey(League)
    team0 = models.OneToOne(Team)
    team1 = models.OneToOne(Team)
    score0 = models.PositiveIntegerField()
    score1 = models.PositiveIntegerField()
    venue = models.ForeignKey(Club)