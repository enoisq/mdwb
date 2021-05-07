from rest_framework import serializers

from .models import Device, Hems_sys, Zone, Outlet
from api_devices.serializers  import DataSerializer
from api_devices.models import Data


class DeviceResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('id', 'devName', 'devType','dev_on')


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('id', 'devName', 'devType', 'dev_on')

class Hems_sysSerializer(serializers.ModelSerializer):
        #outlets = OutletSerializer(many=True)

        class Meta:
            model = Hems_sys
            fields = ('id','hems_last_update','userName',
                      'homeCity','homeStreet','homeNeighbour',
                      'homeComplement','precoKWh')

class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zone
        fields = ('name',)

class OutletResumeSerializer(serializers.ModelSerializer):
    outletZone = serializers.ReadOnlyField(source='outletZone.name')
    connectedDevice = serializers.ReadOnlyField(source='connectedDevice.id')

    class Meta:
        model = Outlet
        fields = ('id','label','outletType','connectedDevice','outletZone')

class OutletSerializer(serializers.ModelSerializer):  # Serializer para a tomada
        outletZone = serializers.ReadOnlyField(source='outletZone.name')
        connectedDevice = serializers.ReadOnlyField(source='connectedDevice.id')
        data = DataSerializer(many=True, read_only=True)

        class Meta:
            model = Outlet
            fields = ('id','label','outletType','connectedDevice','outletZone', 'data')