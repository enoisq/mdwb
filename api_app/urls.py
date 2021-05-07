from django.urls import path, include
from rest_framework import routers

from .views import DeviceViewSet, Hems_sysViewSet, OutletViewSet
#from api_devices.views import DadosViewSet
from api_devices import views
from api_devices.views import RootDataViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'systems_hems', Hems_sysViewSet)
router.register(r'outlets', OutletViewSet)
#router.register(r'datas', DataViewSet)
router.register(r'root-data',RootDataViewSet)

urlpatterns = [
    path('',include(router.urls)),
   # path('data/', views.DadosViewSet, name='data')
]