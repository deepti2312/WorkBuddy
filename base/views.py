from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from base.models import Cities
from base.serializers import CitiesSerializer


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitiesSerializer
    queryset = Cities.objects.all()
