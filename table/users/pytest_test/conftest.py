import pytest
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
def user_incorrect_email():
    return User.objects.create_user(
        username='test_user_incorect',
        email='test_user_incorectexample.com',
        password='Testpas3!',
        date_of_birth='2005-10-10',
    )


@pytest.fixture
def user_incorrect_date_of_birth():
    return User.objects.create_user(
        username='test_user_incorect',
        email='test_user_incorect@example.com',
        password='Testpas3!',
        date_of_birth='2023-10-10'
    )


@pytest.fixture
def user_long_name():
    return User.objects.create_user(
        username='test_user_incorect00001111111111111111111111111111111111111',
        email='test_user_incorect@example.com',
        password='Testpas3!',
        date_of_birth='2000-10-10'
    )


@pytest.fixture
def user_client(user, client):
    client.force_login(user)
    return client
