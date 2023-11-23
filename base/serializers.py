from rest_framework import serializers

from base.models import Cities


class CitiesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Cities
        fields = '__all__'
