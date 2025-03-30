from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from app.pagination import OpenWheelBasePaginator
from app.models import (Circuit,
                        Constructor,
                        Driver,
                        Nationality)
from app.serializers import (CircuitSerializer,
                             ConstructorSerializer,
                             DriverSerializer,
                             NationalitySerializer)


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
        "id",
        "surname",
        "forename",
        "date_of_birth",
        "nationality",
    ]


class ConstructorViewSet(viewsets.ModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer


class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

