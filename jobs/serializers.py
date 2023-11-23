from rest_framework import serializers
from jobs.models import Jobdescription

class JobdescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobdescription
        fields = '__all__'
        