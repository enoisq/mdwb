from django.contrib import admin

from .models import Device, Hems_sys, Zone, Outlet
# Register your models here.


admin.site.register(Device)
admin.site.register(Hems_sys)
admin.site.register(Outlet)
admin.site.register(Zone)