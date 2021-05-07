from rest_framework import serializers

from .models import Initial_config


class Initial_configSerializer(serializers.ModelSerializer):

    class Meta:
        model = Initial_config
        fields = ( 'cloud_interval', 
    'device_interval'
        )