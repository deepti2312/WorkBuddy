from rest_framework import viewsets
from organizations.serializers import OrgSerializer
from organizations.models import Organizations

class OrganizationView(viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrgSerializer

