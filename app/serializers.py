from rest_framework import serializers

from app.models import (
    Circuit,
    Constructor,
    Driver,
    Nationality,
)


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(required=True)
    nationality = serializers.PrimaryKeyRelatedField(queryset=Nationality.objects.all(),
                                                     source="nationality.demonym",
                                                     required=False)
    date_of_birth = serializers.DateField(format="%d-%b-%Y")

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
    country = serializers.PrimaryKeyRelatedField(queryset=Nationality.objects.all(),
                                                 source="country.country",
                                                 required=False)
    coordinates = serializers.StringRelatedField()

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

