from django.core.management.base import BaseCommand
import csv

from tmap.models import ChargingStation


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        data = csv.DictReader(open("dist/data/ev_pos.csv"))
        for row in data:
            ChargingStation.objects.create(
                name=row['NAME'],
                charger_quantity=row['QUANTITY'],
                charger_type=row['TYPE'],
                address=row['ADDRESS'],
                latitude=row['LATITUDE'],
                longitude=row['LONGITUDE'],
            )
