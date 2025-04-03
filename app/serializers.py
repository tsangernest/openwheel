from rest_framework import serializers

from app.models import (Circuit,
                        Constructor,
                        Driver,
                        Nationality,
                        Race,
                        Qualifying)


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

    def get_coordinates(self, obj) -> str:
        return f"{obj.coordinates}"


class RaceSerializer(serializers.ModelSerializer):
    date_of_race = serializers.DateTimeField(format="%d-%b-%Y")
    circuit = serializers.PrimaryKeyRelatedField(queryset=Circuit.objects.all(),
                                                 source="circuit.name",
                                                 required=True)

    class Meta:
        model = Race
        fields = "__all__"


class QualifyingSerializer(serializers.ModelSerializer):
    race = serializers.PrimaryKeyRelatedField(queryset=Qualifying.objects.all(),
                                              source="race.name",
                                              required=True)
    driver = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(),
                                                source="driver.surname",
                                                required=True)
    constructor = serializers.PrimaryKeyRelatedField(queryset=Constructor.objects.all(),
                                                     source="constructor.name",
                                                     required=True)

    class Meta:
        model = Qualifying
        fields = "__all__"

