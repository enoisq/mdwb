from django.urls import path, include
from rest_framework import routers
from .views import Zigbee_configAPIView, DataList
from django.conf.urls import url
from api_devices import views
from django.views.generic import RedirectView

urlpatterns = [
    #path('initial/', Initial_configAPIView.as_view(), name='config'),
    path('interfaces/', Zigbee_configAPIView.as_view(), name='zigbee'),
    #path('dados/', DadosViewSet.as_view(), name='Dados'),
    #path('datas/<int:dev_pk>/', DatasAPIView.as_view(), name ='datas'),
    url(r'^datalist/$', views.DataList.as_view(), name='dadoslist'),
    #path('interfaces/', , name='data')
    #url(r'^datas/$', views.DataViewSet.as_view(), name='datas')
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico'))
]