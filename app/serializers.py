from rest_framework import serializers

from app.models import Nationality


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"

