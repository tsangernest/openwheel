from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from app.pagination import OpenWheelBasePaginator
from app.models import (Circuit,
                        Constructor,
                        Driver,
                        LapTime,
                        Nationality,
                        Race,
                        Qualifying)
from app.serializers import (CircuitSerializer,
                             ConstructorSerializer,
                             DriverSerializer,
                             LapTimeSerializer,
                             NationalitySerializer,
                             RaceSerializer,
                             QualifyingSerializer)


class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    pagination_class = OpenWheelBasePaginator

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]

    ordering_fields = [
        # "id",
        "surname",
        "forename",
        # "date_of_birth",
        # "nationality",
    ]


class ConstructorViewSet(viewsets.ModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer


class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    pagination_class = OpenWheelBasePaginator


class QualifyingViewSet(viewsets.ModelViewSet):
    queryset = Qualifying.objects.all()
    serializer_class = QualifyingSerializer
    pagination_class = OpenWheelBasePaginator


class LapTimeViewSet(viewsets.ModelViewSet):
    queryset = LapTime.objects.all()
    serializer_class = LapTimeSerializer
    pagination_class = OpenWheelBasePaginator

