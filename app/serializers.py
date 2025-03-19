from rest_framework import serializers

from app.models import Driver, Nationality


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    nationality = serializers.PrimaryKeyRelatedField(queryset=Nationality.objects.all(),
                                                     source="nationality.demonym",
                                                     required=False)
    date_of_birth = serializers.DateField(format="%d-%b-%Y")

    class Meta:
        model = Driver
        fields = "__all__"

