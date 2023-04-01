from django.contrib import admin
from .models import Service
# Register your models here.

#gestionar el modelo en el administrador
#clase para realizar la configuracion del modelo en el administrador
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
