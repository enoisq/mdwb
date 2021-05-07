from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Initial_config
from .serializers import Initial_configSerializer
# Create your views here.


class Initial_configAPIView(APIView):
    """
     API de Cadastro de informações HEMS
    """
    def get(self, request):
        initial = Initial_config.objects.all()
        serializer = Initial_configSerializer(initial, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = Initial_configSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)