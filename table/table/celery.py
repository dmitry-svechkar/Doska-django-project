import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table.settings')

app = Celery('table')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.broker_url = os.getenv('LOCATION')
app.conf.result_backend = os.getenv('LOCATION')


app.conf.beat_schedule = {
    'send_email_for_moderator': {
        'task': 'users.tasks.send_email_for_moderator',
        'schedule': crontab(minute='*/60'),
        },
}

app.conf.timezone = 'Europe/Moscow'

# celery -A table worker --loglevel=info -P eventlet  запуск
# celery -A table flower
#  celery -A table beat запуск beat
