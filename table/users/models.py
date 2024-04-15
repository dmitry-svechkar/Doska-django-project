import os

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from dotenv import load_dotenv

from users.validators import validate_age

load_dotenv()


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер.
    Переопределение логики создания пользователей.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Кастомная модель пользователя.
    """
    class Role(models.TextChoices):
        user = 'user'
        MOREDATOR = 'moderator'

    username = models.CharField('Имя пользователя', max_length=40, unique=True)
    email = models.EmailField(
        "Адрес электронной почты",
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField('Прошел регистрацию', default=False)
    date_of_birth = models.DateField(
        'Дата рождения',
        validators=[validate_age,],
    )
    user_info = models.TextField(blank=True)
    role = models.CharField(
        'Роль', max_length=9, choices=(Role.choices), default=Role.user
    )
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def email_user(
        self,
        subject,
        message,
        from_email=os.getenv('DEFAULT_FROM_EMAIL'),
        **kwargs
    ):
        """Отправить письмо с потверждением регистрации."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
