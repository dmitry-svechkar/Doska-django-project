import pytest
from goods.models import GoodCategory, Goods


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
