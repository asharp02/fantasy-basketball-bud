""" 
Management command to fetch NBA player data + stats and store them within
our Player and PlayerStats model.
python manage.py import_player_stats

"""

from django.core.management.base import BaseCommand
from fantasybuddy.models import Player, PlayerStats


class Command(BaseCommand):
    help = "Fetch NBA Player stats and import them into Player + PlayerStats models"

    def handle(self, *args, **options):
        pass
