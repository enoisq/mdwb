from django.db import models
from api_app.models import Outlet
from django_filters import FilterSet

#class DataManager(models.Manager):
#    def entre_datas(self, data_ini, data_fim):
#        self.filter(time__range=(data_ini, data_fim))


# Create your models here.
class Zigbee_interface(models.Model):
    #complement = models.CharField(max_length=30,null=True)
        port = models.CharField(max_length=6)
        pan_id = models.CharField(max_length=6)

        class Meta:
            verbose_name = 'zigbee'
            verbose_name_plural = 'zigbee'

        def __str__(self):
            return f'Coordinator Zigbee foi cadastrado com sucesso!'

class Data(models.Model):
    dev = models.ForeignKey(Outlet, on_delete=models.CASCADE,related_name="data")
    voltage = models.CharField(max_length=255)
    current = models.CharField(max_length=255)
    active_power = models.CharField(max_length=255)
    reactive_power = models.CharField(max_length=255)
    power_factor = models.CharField(max_length=255)
    dev_energy = models.CharField(max_length=6)
    #dev_on = models.BooleanField(default=True)
    time = models.DateTimeField(max_length=70)

    #objects = DataManager()


    class Meta:
        verbose_name = 'data'
        verbose_name_plural = 'datas'

    def __str__(self):
        return f'Datas'

class RootData(models.Model):
    time = models.DateTimeField()
    power = models.CharField(max_length=50)
