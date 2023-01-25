from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(length=100)
    last_name = models.CharField(length=100)
    position = models.CharField(length=5)
    status = models.CharField(length=5)


class PlayerStats(models.Model):
    player = models.ForeignKey(name="Player", on_delete=models.CASCADE)
    timeline = models.CharField(length=5)
    rank = models.PositiveIntegerField()
    field_goal_attempts = models.DecimalField()
    field_goals_made = models.DecimalField()
    ft_attempts = models.DecimalField()
    ft_made = models.DecimalField()
    three_pt_made = models.DecimalField()
    points = models.DecimalField()
    rebounds = models.DecimalField()
    assists = models.DecimalField()
    steals = models.DecimalField()
    blocks = models.DecimalField()
    tos = models.DecimalField()


class FantasyTeam(models.Model):
    team_name = models.CharField(length=100)
    manager = models.ForeignKey(name="Manager", on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)
    league = models.PositiveIntegerField()


class NBATeam(models.Model):
    team_name = models.CharField(length=100)
    players = models.ManyToManyField(Player)


class Game(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey(name="NBATeam", on_delete=models.CASCADE)
    away_team = models.ForeignKey(name="NBATeam", on_delete=models.CASCADE)

    # Find way to ensure home_team and away_team are never the same team
    # Add lots of validation testing for edge cases or weird data import issues (ie.
    # duplicate records for the same game with wrong home_team and away team designations)


class PlayerWaiverStatus(models.Model):
    player = models.ForeignKey(name="Player", on_delete=models.CASCADE)
    league = models.PositiveIntegerField()
    status = models.CharField(length=10)  # FA, Waivers, on a team
