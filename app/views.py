from rest_framework import viewsets

from app.models import Driver, Nationality
from app.serializers import DriverSerializer, NationalitySerializer


class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

