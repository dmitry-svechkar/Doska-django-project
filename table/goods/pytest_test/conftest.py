import pytest
from goods.models import (Goods, GoodCategory, WishGoods,
                          Carts, Orders)
from users.models import User


@pytest.fixture()
def user():
    user = User.objects.create_user(
        username='test_user',
        email='test_user@example.com',
        password='Testpas3!',
        date_of_birth='2000-10-10'
    )
    return user


@pytest.fixture
def user_client(user, client):
    client.force_login(user)
    return user_client


@pytest.fixture
def category():
    category = GoodCategory.objects.create(
        category_good_name='Category1',
        category_description='Category Description',
        is_published=False
    )
    return category


@pytest.fixture
def category_without_description():
    return GoodCategory.objects.create(
        category_good_name='Category2',
        is_published=False
    )


@pytest.fixture
def category_without_name():
    return GoodCategory.objects.create(
        category_description='Category Description',
        is_published=False
    )


@pytest.fixture
def good(user, category):
    return Goods.objects.create(
        good_name='good',
        model='model',
        condition='БУ',
        good_cost=100,
        description='Описание товара',
        good_category=category,
        seller=user
    )


@pytest.fixture
def good_without_user(category):
    return Goods.objects.create(
        good_name='good',
        model='model',
        condition='БУ',
        good_cost=100,
        description='Описание товара',
        good_category=category,
        seller=None
    )


@pytest.fixture
def good_without_name(user, category):
    return Goods.objects.create(
        model='model',
        condition='БУ',
        good_cost=100,
        description='Описание товара',
        good_category=category,
        seller=user
    )


@pytest.fixture
def good_without_category(user, category):
    return Goods.objects.create(
        model='model',
        condition='БУ',
        good_cost=100,
        description='Описание товара',
        seller=user
    )


@pytest.fixture
def wish(good, user):
    return WishGoods.objects.create(
        user=user,
        good=good
    )


@pytest.fixture
def cart(good, user):
    return Carts.objects.create(
        user=user,
        quantity=10,
        good=good
    )


@pytest.fixture
def order(user, cart):
    order = Orders.objects.create(
        full_name=user.username,
        email=user.email,
        phone_number='79551234567',
        city='Moscow',
        address='some_adress 15',
        delivery_method='Курьер',
        user=user
    )
    order.cart.set([cart])
    return order
