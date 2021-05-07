from rest_framework import serializers

from .models import Zigbee_interface, Data, RootData


class Zigbee_configSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zigbee_interface
        fields = ( 'port', 
    'pan_id'
        )


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('dev_id', 'voltage','current','active_power','reactive_power','power_factor','dev_energy','time')
        

class RootDataSerializer(serializers.ModelSerializer):


    class Meta:
        model = RootData
        fields = ('time', 'power')