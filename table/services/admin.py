from django.contrib import admin

from services.models import Services, ServiceCategory


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    pass
