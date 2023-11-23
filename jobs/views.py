from rest_framework import viewsets
from jobs.serializers import JobdescriptionSerializer
from jobs.models import Jobdescription

class JobdescriptionView(viewsets.ModelViewSet):
    queryset = Jobdescription.objects.all()
    serializer_class = JobdescriptionSerializer

