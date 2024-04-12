from django.contrib import admin

from goods.models import (Carts, GoodCategory, Goods,
                          GoodsPhoto, WishGoods, Orders)


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    pass


@admin.register(GoodCategory)
class GoodCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(GoodsPhoto)
class GoodsPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(WishGoods)
class WishGoodsAdmin(admin.ModelAdmin):
    pass


@admin.register(Carts)
class CartsAdmin(admin.ModelAdmin):
    pass


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass
