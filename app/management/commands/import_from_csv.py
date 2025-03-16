import csv

from django.core.management import BaseCommand

from app.models import Nationality


class Command(BaseCommand):
    help = f"Management command to help import csv files"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **options):
        path = options.get("path")

        with open(file=path, mode="r", encoding="utf-8") as file:
            csv_file = csv.reader(file)
            (Nationality
             .objects
             .bulk_create([Nationality(demonym=d, country=c) for d, c in csv_file]))

