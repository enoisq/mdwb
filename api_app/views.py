from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from api_app.models import Device, Hems_sys, Outlet
from .serializers import DeviceSerializer, DeviceResumeSerializer, Hems_sysSerializer, OutletSerializer, OutletResumeSerializer
from rest_framework.filters import SearchFilter
from api_devices.serializers import DataSerializer
from api_devices.models import Data

class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def list(self, request, *args, **kwargs):
        queryset = Device.objects.all()
        serializer = DeviceResumeSerializer(queryset, many=True)
        return Response(serializer.data)


class Hems_sysViewSet(ModelViewSet):
    queryset = Hems_sys.objects.all()
    serializer_class = Hems_sysSerializer
    #permission_classes = [IsAdminUser]

class OutletViewSet(ModelViewSet):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer

    def list(self, request, *args, **kwargs):
       queryset = Outlet.objects.all()
       serializer = OutletResumeSerializer(queryset, many=True)
       return Response(serializer.data)


    @action(detail=True, methods=['get'])
    def data(self, request, pk=None):
        device = self.get_object()
        serializer = DataSerializer(device.data.all(), many=True)
        return Response(serializer.data)

