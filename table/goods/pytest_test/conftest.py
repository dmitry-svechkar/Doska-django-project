import pytest
from goods.models import Goods, GoodCategory
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
