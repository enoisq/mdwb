from django.db import models

# Create your models here.
class Initial_config(models.Model):
    #complement = models.CharField(max_length=30,null=True)
    cloud_interval = models.IntegerField()
    device_interval = models.IntegerField()

    class Meta:
        verbose_name = 'config'
        verbose_name_plural = 'configs'

    def __str__(self):
        return f'{self.cloud_interval} foi cadastrado com sucesso!'
