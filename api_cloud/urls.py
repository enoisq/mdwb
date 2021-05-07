from django.urls import path
from .views import Initial_configAPIView

urlpatterns = [
    path('initial/', Initial_configAPIView.as_view(), name='config'),
    #path('interfaces/', Zigbee_configAPIView.as_view(), name='zigbee')
    #path('hems/', HemsuserAPIView.as_view(), name='hems')
]