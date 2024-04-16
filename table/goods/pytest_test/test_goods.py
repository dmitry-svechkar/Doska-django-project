import pytest
from goods.models import (Goods, GoodCategory, WishGoods,
                          Carts, Orders)


@pytest.mark.django_db
def test_category_is_created(category, category_without_description):
    assert GoodCategory.objects.count() == 1, 'test1'
    assert category.id == 1, 'test2'
    assert category_without_description.id != 2, 'test3'


@pytest.mark.django_db
def test_good_is_created(good, category, user):
    assert Goods.objects.count() == 1, 'test1'
    assert good.id == 1, 'test2'
    assert good.good_category.id == category.id, 'test3'
    assert good.seller == user, 'test4'
    assert good.is_published is False
    assert good.in_stock is False


@pytest.mark.django_db
def test_wish_is_created(wish, good):
    assert WishGoods.objects.count() == 1, 'test1'
    assert wish.id == 1, 'test2'
    assert wish.user.id == 1, 'test3'
    assert wish.good == good, 'test5'


@pytest.mark.django_db
def test_cart_is_created(cart, good, user):
    assert Carts.objects.count() == 1, 'test1'
    assert cart.quantity == 10, 'test2'
    assert cart.good == good, 'test3'
    assert cart.user == user, 'test4'


@pytest.mark.django_db
def test_order_is_created(order, user, good):
    assert Orders.objects.count() == 1, 'test1'
    assert order.id == 1, 'test2'
    assert order.user == user, 'test3'
    assert order.city == 'Moscow', 'test4'
