from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    clubs = models.ManyToMany('Club.models.Club')
    accessLevel = models.PositiveIntegerField()