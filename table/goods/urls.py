from django.urls import path

from goods.views import (AddDeleteCartView, AddGoodsView, AddToWishListView,
                         CartView, GoodDetailView, GoodsListView, WishListView,
                         CategoryView, CheckoutCart, SuccessCart)

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
    path('carts/checkout/success/',
         SuccessCart.as_view(),
         name='success_cart'),
    path('carts/checkout/', CheckoutCart.as_view(), name='checkout_cart'),
    path('carts/', CartView.as_view(), name='carts'),
    path('<slug:slug>/', GoodDetailView.as_view(), name='good-detail'),
    path('add_to_wishlist/<slug:slug>/',
         AddToWishListView.as_view(),
         name='add_to_wishlist'),
    path('', GoodsListView.as_view(), name='goods-list'),
]
