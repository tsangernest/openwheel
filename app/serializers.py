from datetime import datetime
import math

from rest_framework import serializers

from app.models import (Circuit, Constructor, ConstructorStanding, Driver,
                        DriverStanding, DropStuff, LapTime, Nationality,
                        PitStop, Qualifying, Race)


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

# YES
    # def to_internal_value(self, data):
    #     data["ref"] = data["ref"].lower() if data.get("ref") else ""
    #     data["nationality"] = self._get_country_obj(str(data.get("nationality")))
    #
    #     return data

    def to_internal_value(self, data):
        data.update({
            "ref": data["ref"].lower() if data.get("ref") else "",
            "date_of_birth": self._format_date_repr(data["date_of_birth"]),
            "nationality": self._get_country_obj(str(data.get("nationality"))),
        })
        return data

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "ref": instance.ref,
            "number": instance.number,
            "code": instance.code,
            "forename": instance.forename,
            "surname": instance.surname,
            "date_of_birth": instance.date_of_birth.strftime("%Y-%B-%d"),
            "nationality": instance.nationality.country,
            "url": instance.url,
        }

    @staticmethod
    def _format_date_repr(date) -> str | datetime:
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return datetime.strptime(date, "%Y-%B-%d")

    @staticmethod
    def _get_country_obj(country) -> Nationality:
        if country.isnumeric():
            return Nationality.objects.filter(pk=country).first()
        return Nationality.objects.filter(country=country).first()


class ConstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constructor
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "ref": instance.ref,
            "name": instance.name,
            "nationality": instance.nationality.country,
            "url": instance.url,
        }


class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuit
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "country": instance.country.country,
            "location": instance.location,
            "altitude": instance.altitude,
            "coordinates": instance.coordinates,
            "url": instance.url,
        }


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "circuit": instance.circuit.name,
            "date_of_race": instance.date_of_race.strftime(format="%d-%b-%Y"),
            "round_number": instance.round_number,
            "url": instance.url,
        }


class QualifyingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualifying
        fields = "__all__"

    def to_representation(self, instance):
        q_one_pretty = q_two_pretty = q_three_pretty = None

        if instance.q_one:
            q_one_pretty = (f"{math.floor(instance.q_one.seconds / 60)}"
                            f":{instance.q_one.seconds % 60}"
                            f".{instance.q_one.microseconds}")
        if instance.q_two:
            q_two_pretty = (f"{math.floor(instance.q_two.seconds / 60)}"
                            f":{instance.q_two.seconds % 60}"
                            f".{instance.q_two.microseconds}")
        if instance.q_three:
            q_three_pretty = (f"{math.floor(instance.q_three.seconds / 60)}"
                              f":{instance.q_three.seconds % 60}"
                              f".{instance.q_three.microseconds}")

        return {
            "id": instance.id,
            "race": instance.race.name,
            "driver": instance.driver.surname,
            "constructor": instance.constructor.name,
            "q_one": q_one_pretty,
            "q_two": q_two_pretty,
            "q_three": q_three_pretty,
            "position": instance.position,
        }


class LapTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LapTime
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "race": instance.race.name,
            "driver": instance.driver.surname,
            "lap_number": instance.lap_number,
            "position": instance.position,
            "time": f"{math.floor(instance.time.seconds / 60)}:{instance.time.seconds % 60}.{instance.time.microseconds}",
        }


class PitStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PitStop
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "race": instance.race.name,
            "driver": instance.driver.surname,
            "stop_number": instance.stop_number,
            "lap_number": instance.lap_number,
            "local_time": instance.local_time.strftime(format="%H:%M:%S"),
            "time": instance.duration,
        }


class DriverStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverStanding
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "race": instance.race.name,
            "driver": instance.driver.surname,
            "points": instance.points,
            "number_of_wins": instance.number_of_wins,
        }


class ConstructorStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructorStanding
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "race": instance.race.name,
            "constructor": instance.constructor.name,
            "points": instance.points,
            "number_of_wins": instance.number_of_wins,
        }


class DropStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropStuff
        fields = "__all__"

