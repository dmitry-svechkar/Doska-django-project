from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from goods.views import (AddDeleteCartView, AddGoodsView, AddToWishListView,
                         CartView, GoodDetailView, GoodsListView, WishListView,
                         CategoryView)

urlpatterns = [
    path(
        'add_advertisment/',
        AddGoodsView.as_view(),
        name='add-advertisment'
    ),
    path(
         'categories/<slug:category_slug>',
         CategoryView.as_view(),
         name='categories'
    ),
    path('wish_list/', WishListView.as_view(), name='wish_list'),
    path('add_to_cart/<slug:slug>/',
         AddDeleteCartView.as_view(),
         name='add_to_cart'),
    path('delete_from_cart/<slug:slug>/',
         AddDeleteCartView.as_view(),
         name='delete_from_cart'),
    path('carts/', CartView.as_view(), name='carts'),
    path('<slug:slug>/', GoodDetailView.as_view(), name='good-detail'),
    path('add_to_wishlist/<slug:slug>/',
         AddToWishListView.as_view(),
         name='add_to_wishlist'),
    path('', GoodsListView.as_view(), name="goods-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
