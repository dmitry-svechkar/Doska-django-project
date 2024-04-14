import os
from celery import shared_task
from goods.models import Goods
from django.core.mail import send_mail


def get_object_good(goods_id):
    """ Получаем объект товара. """
    goods = Goods.objects.get(id=goods_id)
    return goods


def get_recipient_email(goods):
    """ Получаем объект почты продавца. """
    return goods.seller.email


def get_order_and_cart_object(user):
    """ Получаем объекты заказа и корзины. """
    from goods.models import Orders
    order = Orders.objects.filter(user_id=user).last()
    goods_in_order = Orders.objects.filter(user_id=user).values('cart__good')
    return [order, goods_in_order]


@shared_task
def send_published_notification(good_id, **kwargs):
    """ Отправляем сообщение о публикации товара на сайте. """
    good = get_object_good(good_id)
    subject = 'Ваш товар опубликован'
    message = f'Ваш товар "{good.good_name}" был успешно опубликован.'
    from_email = os.getenv('DEFAULT_FROM_EMAIL')
    recipient = get_recipient_email(good)
    send_mail(subject, message, from_email, [recipient],  **kwargs)


@shared_task
def send_new_good_notification(good_id):
    """
    Отправляем сообщение о загрузке товара на сайти ожидаением потверждения.
    """
    good = get_object_good(good_id)
    subject = 'Информация о размещении товара'
    message = f'''Ваш товар "{good.good_name}" был загружен на сайт.
    Дождитесь потверждения модератора и он появится на сайте.'''
    from_email = os.getenv('DEFAULT_FROM_EMAIL')
    recipient = get_recipient_email(good)
    try:
        send_mail(subject, message, from_email, [recipient])
    except Exception:
        return False
    else:
        return True


@shared_task
def block_good_for_break_rules(good_id, **kwargs):
    """ Отправляем сообщение о блокировки товаров с причиной. """
    good = get_object_good(good_id)
    subject = 'Ваш товар временно заблокирован'
    message = f'''Ваш товар "{good.good_name}" был временно заблокирован.
    причина {good.reason_for_not_publish}.
    Внесите необходимые изменения.'''
    from_email = os.getenv('DEFAULT_FROM_EMAIL')
    recipient = get_recipient_email(good)
    send_mail(subject, message, from_email, [recipient],  **kwargs)


@shared_task
def send_mail_new_order_to_costumer(user, **kwargs):
    """ Отправляем сообщение покупателю с информацией о заказе. """
    order = get_order_and_cart_object(user)[0]
    goods_in_order = get_order_and_cart_object(user)[1]
    goods = ''
    for item in goods_in_order:
        good_id = item['cart__good']
        good = get_object_good(good_id)
        goods += f'Товар - {good.good_name} - стоимость - {good.good_cost}\n'

    subject = 'Вы оформили заказ'
    message = f'''
    {order.user.username}, ваш заказ принят.
    адрес доставки {order.city}, {order.address},
    {goods}
    С вами свяжется продавец, способ доставки {order.delivery_method}
    '''
    from_email = os.getenv('DEFAULT_FROM_EMAIL')
    recipient = order.user
    send_mail(subject, message, from_email, [recipient],  **kwargs)


@shared_task
def send_mail_for_seller(user):
    """ Отправляем сообщение продавцу с информацией о заказе. """
    order = get_order_and_cart_object(user)[0]
    goods_in_order = get_order_and_cart_object(user)[1]
    for item in goods_in_order:
        good_id = item['cart__good']
        good = get_object_good(good_id)
        recipient = get_recipient_email(good)
        subject = 'Вы получили заказ'
        message = f'''
        Покупатель {order.full_name}, Контакт {order.phone_number}
        адрес доставки {order.city}, {order.address},
        Состав заказа: {good.good_name}
        Cпособ доставки {order.delivery_method}
        '''
        from_email = os.getenv('DEFAULT_FROM_EMAIL')
        send_mail(subject, message, from_email, [recipient],)
