import json
import requests
from django.core.management.base import BaseCommand
from NBAStats.models import Players

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = 'https://api.sportsdata.io/v3/nba/scores/json/PlayersActiveBasic?key=da686a4686694616bc1338e51da098f3'
        response = requests.get(url)
        data = response.json()

        for item in data:
            player = Players.objects.create(
                first_name=item.get('FirstName', ''),
                last_name=item.get('LastName', ''),
                jersey_number=item.get('Jersey', ''),
                position=item.get('Position', ''),
                weight=item.get('Weight', 0.0),
                height=item.get('Height', ''),
                ppg=item.get('PointsPerGame', 0.0),
                apg=item.get('AssistsPerGame', 0.0),
                rpg=item.get('ReboundsPerGame', 0.0),
                spg=item.get('StealsPerGame', 0.0),
                bpg=item.get('BlocksPerGame', 0.0),
                field_goal_percent=item.get('FieldGoalsPercentage', 0.0),
                three_pointer_percent=item.get('ThreePointersPercentage', 0.0),
                free_throw_percent=item.get('FreeThrowsPercentage', 0.0),
                turnovers=item.get('TurnoversPerGame', 0.0),
                minutes_played=item.get('MinutesPerGame', 0.0)
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully added {player}'))