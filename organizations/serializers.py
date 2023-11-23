from rest_framework import serializers
from organizations.models import Organizations

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = '__all__'