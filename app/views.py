from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from app.models import Driver, Nationality
from app.serializers import DriverSerializer, NationalitySerializer
from app.pagination import OpenWheelBasePaginator


class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    # pagination_class = None
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

