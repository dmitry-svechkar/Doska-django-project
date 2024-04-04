from django.db import models
from slugify import slugify
from users.models import User


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаги опубликовано и Добавлено."""

    is_published = models.BooleanField(
        'Опубликовано',
        default=False,
        help_text='Поставьте галочку, чтобы  опубликовать.',
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

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

    def save(self, *args, **kwargs):
        if not self.category_description:
            return None
        super(GoodCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_good_name


class Goods(PublishedModel):
    """ Модель товаров. """
    CONDITION_GOOD_CHOICES = [
        ('Новое', 'NEW'),
        ('БУ', 'USED')
    ]
    good_name = models.CharField('Наименование товара', max_length=100)
    model = models.CharField(
        'Модель товара',
        max_length=100,
        null=True,
        blank=True
    )
    condition = models.CharField(max_length=5, choices=CONDITION_GOOD_CHOICES)
    in_stock = models.BooleanField(default=False)
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
        related_name='goods'
    )
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='seller'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.seller.username + '-' + self.good_name)
        super(Goods, self).save(*args, **kwargs)

    def __str__(self):
        return self.good_name


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
        related_name='goods')

    def __str__(self):
        return f'фото {self.good.good_name}'


class AbstactUserGoodModel(models.Model):
    """ Класс миксин для вынесения сущностей связи с моделями User и Goods. """
    user = models.ForeignKey(User,
                             related_name='wishes',
                             on_delete=models.CASCADE)
    good = models.ForeignKey(Goods,
                             related_name='wishes',
                             on_delete=models.CASCADE)


class WishGoods(AbstactUserGoodModel):
    """ Модель сущностей желаемых товаров. """
    class Meta:
        default_related_name = 'wishes'
        verbose_name = 'желаемый товар'
        verbose_name_plural = 'желаемые товары'

    def __str__(self):
        return f'''
    Пользователь {self.user.username}
    добавил в список желаемого {self.good.good_name}
    '''


class Carts(AbstactUserGoodModel):
    """ Модель сущностей  списка покупок. """
    quantity = models.SmallIntegerField()

    class Meta:
        default_related_name = 'carts'
        verbose_name = 'список покупок'
        verbose_name_plural = 'список покупок'

    def __str__(self):
        return f'''
    Пользователь {self.user.username}
    добавил в список желаемого {self.good.good_name}
    '''
