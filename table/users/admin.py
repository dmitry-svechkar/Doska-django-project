from django.contrib import admin

from users.models import User


@admin.register(User)
class SellerAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'is_active',
        'role'
    )
    list_filter = ('username', 'email', 'role')
    search_fields = ('username',)
    ordering = ('-last_login',)
    fields = [
        ('username', 'email'),
        'role', 'groups',
        ('is_active', 'is_superuser')
    ]
