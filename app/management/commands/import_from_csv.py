import csv

from django.core.management import BaseCommand

from app.models import Driver, Nationality


class Command(BaseCommand):
    help = f"Management command to help import csv files"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **options):
        path = options.get("path")

        # get nationalities
        # with open(file=path, mode="r", encoding="utf-8") as file:
        #     csv_file = csv.reader(file)
        #     (Nationality
        #      .objects
        #      .bulk_create([Nationality(demonym=d, country=c) for d, c in csv_file]))

        # get drivers
        with open(file=path, mode="r", encoding="utf-8") as file:
            csv_file = csv.reader(file)
            column_names = next(csv_file)
            driver_objs = []

            for id, ref, num, code, first, last, dob, nation, url in csv_file:
                n = Nationality.objects.filter(demonym=nation).first()
                d = Driver(id=id,
                           ref=ref,
                           number=num,
                           code=code,
                           forename=first,
                           surname=last,
                           nationality=n,
                           date_of_birth=dob,
                           url=url)
                driver_objs.append(d)

            Driver.objects.bulk_create(driver_objs)

