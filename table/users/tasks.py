import os
from goods.models import User
from django.core.mail import send_mail
from table.celery import app


@app.task
def send_email_for_moderator():
    """
    Отправка сообщения группе модераторов
    раз в 1 час с ссылкой на админку для модерации новых объявлений.
    """
    moderators = User.objects.get(role='moderator')
    subject = 'модерация '
    message = '''
    Перерейдите по ссылке и проведите модерацию объявлений.
    http://127.0.0.1:8000/admin/goods/goods/
    {site}
    '''
    from_email = os.getenv('DEFAULT_FROM_EMAIL')
    recipient = moderators.email
    send_mail(subject, message, from_email, [recipient])
