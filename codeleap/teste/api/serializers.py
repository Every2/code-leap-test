from rest_framework import serializers
from teste import models

class DataStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataStructure
        fields = '__all__'
