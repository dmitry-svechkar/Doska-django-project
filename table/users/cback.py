from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameModelBackend(ModelBackend):
    '''
    Кастомный backend для авторизации по почте
    или логину на выбор пользователя.
    '''
    UserModel = get_user_model()

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = self.UserModel.objects.get(username=username)
        except self.UserModel.DoesNotExist:
            try:
                user = self.UserModel.objects.get(email=username)
            except self.UserModel.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None
