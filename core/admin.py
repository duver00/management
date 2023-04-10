from django.contrib import admin
from .models import Drone, Medication
# Register your models here.

class DroneAdmin(admin.ModelAdmin):
    list_display = ('serial_number','state','battery_capacity','weight_limit')



class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name','weight','code')


admin.site.register(Drone,DroneAdmin)
admin.site.register(Medication,MedicationAdmin)