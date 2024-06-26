from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from slugify import slugify

from users.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаги опубликовано и Добавлено."""
    reason = [
        ('Нарушает правило сайта', 'Нарушает правило сайта'),
        ('Не соответствует действительности',
         'Не соответствует действительности'),
        ('Ненормативная лексика', 'Ненормативная лексика'),
        ('Другая причина', 'Другая причина')

    ]
    is_published = models.BooleanField(
        'Опубликовано',
        default=False,
        help_text='Поставьте галочку, чтобы  опубликовать.',
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    reason_for_not_publish = models.CharField(
        'Причина непубликации',
        max_length=100,
        choices=reason,
        null=True,
        default=False,
        blank=True
    )

    class Meta:
        abstract = True


class GoodCategory(PublishedModel):
    """ Модель категорий товаров. """
    category_good_name = models.CharField(
        'Наименование категории',
        max_length=100
    )
    category_description = models.TextField(
        'Описание группы товаров',
        max_length=500,
        null=False,
    )
    category_slug = models.SlugField(
        'Идентификатор категории',
        unique=True,
    )

    def save(self, *args, **kwargs):
        if not self.category_description:
            return None
        super(GoodCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_good_name

    class Meta:
        verbose_name = ('категория товаров')
        verbose_name_plural = ('категории товаров')


class Goods(PublishedModel):
    """ Модель товаров. """
    CONDITION_GOOD_CHOICES = [
        ('NEW', 'Новое'),
        ('USED', 'БУ')
    ]

    good_name = models.CharField('Наименование товара', max_length=100)
    model = models.CharField(
        'Модель товара',
        max_length=100,
        null=True,
        blank=True
    )
    condition = models.CharField(max_length=5, choices=CONDITION_GOOD_CHOICES)
    in_stock = models.BooleanField('в наличии', default=False)
    good_cost = models.IntegerField(
        'Стоимость товара',
    )
    description = models.TextField('Описание товара', max_length=500)
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        null=True,
    )
    good_category = models.ForeignKey(
        GoodCategory,
        on_delete=models.SET,
        related_name='goods',
        verbose_name='категория товара'
    )
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='seller',
        verbose_name='продавец'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.seller.username + '-' + self.good_name)
        super(Goods, self).save(*args, **kwargs)

    def __str__(self):
        return self.good_name

    class Meta:
        verbose_name = ('товар')
        verbose_name_plural = ('товары')


from goods.tasks import (send_published_notification,
                         block_good_for_break_rules)


@receiver(post_save, sender=Goods)
def send_notification_on_publish(sender, instance, **kwargs):
    if instance.is_published and instance.in_stock:
        send_published_notification.delay(instance.id)


@receiver(post_save, sender=Goods)
def send_mail_cus_block_good(sender, instance, **kwargs):
    if not instance.is_published and instance.reason_for_not_publish:
        block_good_for_break_rules.delay(instance.id)


class GoodsPhoto(PublishedModel):
    """
    Модель добавления фото товаров.
    Реализована возможность добавления сращу нескольких фото к товару.
    """
    good_photo = models.ImageField(
        'Изображение товара',
        upload_to='media/goods/',
        blank=True,
        null=True,
    )
    good = models.ForeignKey(
        Goods,
        on_delete=models.CASCADE,
        related_name='goods',
        verbose_name='товар')

    def __str__(self):
        return f'фото {self.good.good_name}'

    class Meta:
        verbose_name = ('фото')
        verbose_name_plural = ('Архив фото товаров')


class AbstactUserGoodModel(models.Model):
    """ Класс миксин для вынесения сущностей связи с моделями User и Goods. """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='пользователь')
    good = models.ForeignKey(Goods,
                             on_delete=models.CASCADE,
                             verbose_name='товар')

    class Meta:
        abstract = True


class WishGoods(AbstactUserGoodModel):
    """ Модель сущностей желаемых товаров. """

    def __str__(self):
        return f'''
    Пользователь {self.user.username}
    добавил в список желаемого {self.good.good_name}
    '''

    class Meta:
        default_related_name = 'wishes'
        verbose_name = 'желаемый товар'
        verbose_name_plural = 'желаемые товары'


class Carts(AbstactUserGoodModel):
    """ Модель сущностей  списка покупок. """
    quantity = models.SmallIntegerField('кол-во товара',)

    class Meta:
        default_related_name = 'carts'
        verbose_name = 'список покупок'
        verbose_name_plural = 'список покупок'

    def __str__(self):
        return f'''
    Пользователь {self.user.username}
    добавил в список желаемого {self.good.good_name}
    '''


class Orders(models.Model):
    """ Модель сохраняющая информация о сделанном заказе. """
    DELIVERY_METHOD = [
        ('Почта', 'Почта'),
        ('Курьер', 'Курьер')
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(region='RU', max_length=12)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    delivery_method = models.CharField(max_length=6, choices=DELIVERY_METHOD)
    cart = models.ManyToManyField(Carts, related_name='cart')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('заказ')
        verbose_name_plural = ('заказы')
