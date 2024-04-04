from django.db import models
from goods.models import PublishedModel
from users.models import User


class ServiceCategory(PublishedModel):
    """ Модель категорий услуг. """
    CATEGORY_SERVICE_CHOISES = [
        ('BUILDING', 'BUILDING'),
        ('HOME_DEALS', 'HOME_DEALS'),
        ('TEACHING', 'TEACHING'),
        ('RENTING', 'RENTING'),
        ('OTHER', 'OTHER')
    ]

    category_service_name = models.CharField(
        max_length=10,
        choices=CATEGORY_SERVICE_CHOISES
    )

    def __str__(self):
        return self.category_service_name


class Services(PublishedModel):
    """ Модель услуг. """
    service_name = models.CharField(max_length=120)
    service_description = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    service_cost = models.IntegerField(default=0)
    service_category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET,
        related_name='services'
    )
    user_services = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_services'
    )

    def __str__(self):
        return self.service_name
