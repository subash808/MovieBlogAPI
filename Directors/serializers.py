from rest_framework import serializers
from .models import Directors

class DirectorsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Directors
        fields = '__all__' 