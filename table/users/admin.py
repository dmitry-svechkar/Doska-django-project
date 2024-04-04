from django.contrib import admin

from users.models import User


@admin.register(User)
class SellerAdmin(admin.ModelAdmin):
    pass
