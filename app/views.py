from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from app.models import (Circuit, Constructor, ConstructorStanding, Driver,
                        DriverStanding, DropStuff, LapTime, Nationality,
                        PitStop, Qualifying, Race)
from app.pagination import OpenWheelBasePaginator
from app.serializers import (CircuitSerializer, ConstructorSerializer,
                             ConstructorStandingSerializer, DriverSerializer,
                             DriverStandingSerializer, DropStuffSerializer,
                             LapTimeSerializer, NationalitySerializer,
                             PitStopSerializer, QualifyingSerializer,
                             RaceSerializer)


class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer

    def filter_queryset(self, queryset):
        return queryset.filter(deleted_at__isnull=True)


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


class PitStopViewSet(viewsets.ModelViewSet):
    queryset = PitStop.objects.all()
    serializer_class = PitStopSerializer
    pagination_class = OpenWheelBasePaginator


class DriverStandingViewSet(viewsets.ModelViewSet):
    queryset = DriverStanding.objects.all()
    serializer_class = DriverStandingSerializer
    pagination_class = OpenWheelBasePaginator


class ConstructorStandingViewSet(viewsets.ModelViewSet):
    queryset = ConstructorStanding.objects.all()
    serializer_class = ConstructorStandingSerializer


class UploadView(generics.CreateAPIView):
    queryset = DropStuff.objects.all()
    serializer_class = DropStuffSerializer

    def create(self, request, *args, **kwargs):
        file_uploaded = request.FILES.get("file")
        content_type = file_uploaded.content_type
        print(f"\n{content_type=}\n")


        return Response(status=HTTP_200_OK)

