from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django.views import View
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .models import Zigbee_interface, Data, RootData
from .serializers import Zigbee_configSerializer, DataSerializer, RootDataSerializer
from django.http import JsonResponse
# Create your views here.
from datetime import datetime
from time import gmtime, strftime
from django_filters import rest_framework as filters
from rest_framework import generics


class FilterData(filters.FilterSet):
   
    id = filters.NumberFilter(field_name="dev_id", lookup_expr='id')
#    date_gte = filters.DateFilter(field_name="date", lookup_expr='gte')
#    date_lte = filters.DateFilter(field_name="date", lookup_expr='lte')
    date_gte = filters.DateTimeFilter(field_name="time", lookup_expr='gte')
    date_lte = filters.DateTimeFilter(field_name="time", lookup_expr='lte')
    
    class Meta:

        model = Data
        fields = '__all__'


class DataList(generics.ListCreateAPIView):

    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    filter_class = FilterData

class Zigbee_configAPIView(APIView):
    """
     API de Configuração da Interface Zigbee Coordinator
    """
    def get(self, request):
        initial = Zigbee_interface.objects.all()
        serializer = Zigbee_configSerializer(initial, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = Zigbee_configSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RootDataViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    queryset = RootData.objects.all()
    serializer_class = RootDataSerializer