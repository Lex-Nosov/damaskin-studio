from django.contrib import admin

from .models import Services, Clients, Master, Sessions


@admin.register(Services)
class MainAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_description', 'service_cost', 'service_duration']


@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    pass


@admin.register(Sessions)
class SessionAdmin(admin.ModelAdmin):
    pass
