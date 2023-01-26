from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=5)
    status = models.CharField(max_length=5)


class PlayerStats(models.Model):
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    timeline = models.CharField(max_length=5)
    rank = models.PositiveIntegerField()
    field_goal_attempts = models.DecimalField(max_digits=4, decimal_places=2)
    field_goals_made = models.DecimalField(max_digits=4, decimal_places=2)
    ft_attempts = models.DecimalField(max_digits=4, decimal_places=2)
    ft_made = models.DecimalField(max_digits=4, decimal_places=2)
    three_pt_made = models.DecimalField(max_digits=4, decimal_places=2)
    points = models.DecimalField(max_digits=4, decimal_places=2)
    rebounds = models.DecimalField(max_digits=4, decimal_places=2)
    assists = models.DecimalField(max_digits=4, decimal_places=2)
    steals = models.DecimalField(max_digits=4, decimal_places=2)
    blocks = models.DecimalField(max_digits=4, decimal_places=2)
    tos = models.DecimalField(max_digits=4, decimal_places=2)


# do we need this or will this be dynamically fetched
# class FantasyTeam(models.Model):
#     team_name = models.CharField(max_length=100)
#     manager = models.ForeignKey("Manager", on_delete=models.CASCADE)
#     players = models.ManyToManyField(Player)
#     league = models.PositiveIntegerField()


# class NBATeam(models.Model):
#     team_name = models.CharField(max_length=100)
#     players = models.ManyToManyField(Player)


# class Game(models.Model):
#     date = models.DateField()
#     home_team = models.ForeignKey("NBATeam", on_delete=models.CASCADE)
#     away_team = models.ForeignKey("NBATeam", on_delete=models.CASCADE)

# Find way to ensure home_team and away_team are never the same team
# Add lots of validation testing for edge cases or weird data import issues (ie.
# duplicate records for the same game with wrong home_team and away team designations)


class PlayerWaiverStatus(models.Model):
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    league = models.PositiveIntegerField()
    status = models.CharField(max_length=10)  # FA, Waivers, on a team
