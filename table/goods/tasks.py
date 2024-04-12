import os
from celery import shared_task
from goods.models import Goods
from django.core.mail import send_mail


@shared_task
def send_published_notification(goods_id, **kwargs):
    goods = Goods.objects.get(id=goods_id)
    subject = 'Ваш товар опубликован'
    message = f'Ваш товар "{goods.good_name}" был успешно опубликован.'
    from_email = os.getenv('DEFAULT_FROM_EMAIL')
    recipient = goods.seller.email
    send_mail(subject, message, from_email, [recipient],  **kwargs)


@shared_task
def send_new_good_notification(good_id):
    """
    Отправляем сообщение о загрузке товара на сайти ожидаением потверждения.
    """
    good = Goods.objects.get(id=good_id)
    subject = 'Информация о размещении товара'
    message = f'''Ваш товар "{good.good_name}" был загружен на сайт.
    Дождитесь потверждения модератора и он появится на сайте.'''
    from_email = os.getenv('DEFAULT_FROM_EMAIL')
    recipient = good.seller.email
    try:
        send_mail(subject, message, from_email, [recipient])
    except Exception:
        return False
    else:
        return True


@shared_task
def block_good_for_break_rules(goods_id, **kwargs):
    """ Отправляем сообщение о блокировки товаров с причиной. """
    goods = Goods.objects.get(id=goods_id)
    subject = 'Ваш товар временно заблокирован'
    message = f'''Ваш товар "{goods.good_name}" был временно заблокирован.
    причина {goods.reason_for_not_publish}.
    Внесите необходимые изменения.'''
    from_email = os.getenv('DEFAULT_FROM_EMAIL')
    recipient = goods.seller.email
    send_mail(subject, message, from_email, [recipient],  **kwargs)
