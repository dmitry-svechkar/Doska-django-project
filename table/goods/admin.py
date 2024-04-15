from django.contrib import admin
from goods.models import (Carts, GoodCategory, Goods,
                          GoodsPhoto, WishGoods, Orders)


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = (
        'good_name',
        'model',
        'condition',
        'in_stock',
        'good_cost',
        'description',
        'good_category',
        'seller',
        'is_published',
        'reason_for_not_publish'
    )
    search_fields = ('good_name',)
    list_filter = (
        'condition',
        'in_stock',
        'condition',
        'good_category'
    )
    fields = (
        ('is_published', 'reason_for_not_publish'),
        'good_name',
        'model',
        'condition',
        'in_stock',
        'good_cost',
        'description',
        'good_category')


@admin.register(GoodCategory)
class GoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_good_name',
        'category_description',
        'category_slug',
        'is_published',
    )


@admin.register(GoodsPhoto)
class GoodsPhotoAdmin(admin.ModelAdmin):
    list_display = ('good_photo', 'good',)


@admin.register(WishGoods)
class WishGoodsAdmin(admin.ModelAdmin):
    list_display = ('good', 'total_in_wishes',)
    readonly_fields = (('good', 'user'))

    def total_in_wishes(self, obj):
        return obj.good.wishes.count()


@admin.register(Carts)
class CartsAdmin(admin.ModelAdmin):
    list_display = ('good', 'quantity',)
    readonly_fields = ('good', 'user')
    fields = ('quantity', 'good', 'user')


class CartsInline(admin.StackedInline):
    model = Carts
    readonly_fields = ('good', 'user',)
    extra = 0


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'city',
        'address',
        'delivery_method',
        'objects',
    )
    fields = [
        ('full_name', 'email', 'phone_number'),
        ('city', 'address', 'delivery_method'),
    ]
    search_fields = ('email', 'objects')

    def objects(self, obj):
        product_names = []
        for cart in obj.cart.all():
            product_names.append(
                f'id {cart.good.id} {cart.good.good_name} - {cart.quantity}шт'
            )
        return product_names
    objects.short_description = 'товары в заказе'
