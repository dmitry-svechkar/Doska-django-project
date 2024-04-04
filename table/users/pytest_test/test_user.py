import pytest
from datetime import datetime
from users.models import User
from django.urls import reverse
from pytest_django.asserts import assertRedirects


def is_date_of_birth_valid(date_of_birth):
    today = datetime.today()
    res = today.year - datetime.strptime(date_of_birth, '%Y-%m-%d').year
    return res


@pytest.mark.django_db
def test_my_user(user):
    assert user.is_superuser == 0
    assert user.is_active == 0
    assert user.is_staff == 0
    assert user.role == 'user'
    assert is_date_of_birth_valid(user.date_of_birth) > 18
    assert len(user.username) <= 40
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_bad_email(user_incorrect_email):
    assert User.objects.filter(email=user_incorrect_email).exists()


@pytest.mark.django_db
def test_user_bad_date_of_birth(user_incorrect_date_of_birth):
    assert not is_date_of_birth_valid(
        user_incorrect_date_of_birth.date_of_birth
    ) > 18


@pytest.mark.django_db
def test_user_long_username(user_long_name):
    assert not len(user_long_name.username) <= 40


@pytest.mark.django_db
def test_login_page(client, user_client):
    response = client.get(reverse('login'))
    response_auth = user_client.get(reverse('login'))
    assert response.status_code == 200
    assert response_auth.status_code == 200


@pytest.mark.django_db
def test_register_page(client, user_client):
    response = client.get(reverse('django_registration_register'))
    response_auth = user_client.get(reverse('django_registration_register'))
    assert response.status_code == 200
    assert response_auth.status_code == 200
    # assertRedirects(
    #     response_auth,
    #     expected_url=reverse('goods-list'),
    #     status_code=302,
    #     target_status_code=200)


@pytest.mark.django_db
def test_main(client, user_client):
    response = client.get(reverse('main'))
    response_auth = user_client.get(reverse('main'))
    assert response.status_code == 200
    assert response_auth.status_code == 200
