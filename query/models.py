from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Competition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class FooTballer(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    competition = models.ManyToManyField(Competition)
    age = models.IntegerField(default = 18)
    season_goals = models.IntegerField(default = 0)
    seasson_assists = models.IntegerField(default = 0)

    def __str__(self):
        return self.name