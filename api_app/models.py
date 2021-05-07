from django.db import models
#from api_devices.models import Data

# Create your models here.
class Device(models.Model):
    TYPE_CHOICES = (
        ('Generacao', 'Geração'),
        ('Consumo', 'Consumo')
    )
    devName = models.CharField(max_length=30)
    devType = models.CharField(max_length=60, choices=TYPE_CHOICES)
    dev_on = models.BooleanField(default=True)

    class Meta:
        verbose_name='Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.devName

class Hems_sys(models.Model):
    hems_reg_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    userName = models.CharField(max_length=30,default='')
    precoKWh = models.DecimalField(decimal_places=3,max_digits=5)
    hems_last_update = models.DateTimeField()
    homeCity = models.CharField(max_length=30,default='')
    homeStreet = models.CharField(max_length=30,default='')
    homeNeighbour = models.CharField(max_length=20,default='')
    homeComplement = models.CharField(max_length=7,default='')
    #outlets = models.ManyToManyField(Outlet)

    def __str__(self):
        return "Hems "+str(self.id)

class Zone(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Outlet(models.Model):
    TYPE_CHOICES = (
        ('rele', 'Rele'),
        ('dimmer', 'Dimmer')
    )
    label  = models.CharField(max_length=50,null=True,blank=True)
    outletType = models.CharField(max_length=60, choices=TYPE_CHOICES)
    outletZone = models.ForeignKey(Zone,on_delete=models.CASCADE,related_name='outletZone')
    connectedDevice = models.ForeignKey(Device,on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self):
        return "Outlet "+(self.label)