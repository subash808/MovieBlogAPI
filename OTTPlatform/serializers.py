from rest_framework import serializers
from .models import OTTPlatform


class OTTPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = OTTPlatform
        fields = '__all__'