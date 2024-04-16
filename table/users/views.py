from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django_registration.backends.activation.views import RegistrationView

from users.forms import CustomAuthenticationForm


class RegistrationView(RegistrationView):

    def dispatch(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('goods-list'))
        else:
            return super().dispatch(request)


class MyLoginView(LoginView):
    """ Вью аутентификации пользователя. """
    form_class = CustomAuthenticationForm
    template_name = 'site/login.html'
    success_url = '/goods-list/'

    def dispatch(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        else:
            return super().dispatch(request)
