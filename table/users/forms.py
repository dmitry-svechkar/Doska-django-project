from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django_registration.forms import RegistrationForm

from users.models import User


class CustomAuthenticationForm(AuthenticationForm):
    """
    Форма аутентификации посредством Email
    или логина по выбору пользователя.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Login or Email'

    def clean_username(self):
        username = self.cleaned_data.get("username").lower()
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        return email


class MyCustomUserForm(RegistrationForm):
    """
    Форма геристрации пользователя.
    """
    date_of_birth = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"})
    )

    class Meta(RegistrationForm.Meta):
        model = User
        fields = [
            'email',
            'username',
            'date_of_birth'
        ]

    def clean_username(self):
        username = self.cleaned_data.get("username").lower()
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        return email
