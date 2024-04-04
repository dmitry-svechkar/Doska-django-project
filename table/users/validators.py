from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_age(value):
    today = date.today()
    age = today.year - value.year - (
        (today.month, today.day) < (value.month, value.day)
    )
    if age < 18:
        raise ValidationError(
            ('Вам должно быть 18 и более лет'),
        )
