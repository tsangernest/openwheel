from rest_framework import serializers

from app.models import Driver, Nationality


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

