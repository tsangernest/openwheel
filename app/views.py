from rest_framework import viewsets

from app.models import Nationality
from app.serializers import NationalitySerializer


class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer

