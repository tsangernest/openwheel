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
    surname = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(format="%d-%b-%Y")
    nationality = serializers.PrimaryKeyRelatedField(queryset=Nationality.objects.all(),
                                                     source="nationality.demonym",
                                                     required=False)

    class Meta:
        model = Driver
        fields = "__all__"


class ConstructorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    nationality = serializers.PrimaryKeyRelatedField(queryset=Nationality.objects.all(),
                                                     source="nationality.demonym",
                                                     required=False)

    class Meta:
        model = Constructor
        fields = "__all__"


class CircuitSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    coordinates = serializers.StringRelatedField()
    country = serializers.PrimaryKeyRelatedField(queryset=Nationality.objects.all(),
                                                 source="country.country",
                                                 required=False)

    class Meta:
        model = Circuit
        fields = [
            "id",
            "name",
            "country",
            "location",
            "altitude",
            "coordinates",
            "url",
        ]


class RaceSerializer(serializers.ModelSerializer):
    date_of_race = serializers.DateTimeField(format="%d-%b-%Y")
    circuit = serializers.PrimaryKeyRelatedField(queryset=Circuit.objects.all(),
                                                 source="circuit.name",
                                                 required=True)

    class Meta:
        model = Race
        fields = "__all__"


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
    local_time = serializers.TimeField(format="%H:%M:%S")

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
            "local_time": instance.local_time,
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

