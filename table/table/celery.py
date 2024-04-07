import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table.settings')

app = Celery('table')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.broker_url = os.getenv('LOCATION')
app.conf.result_backend = os.getenv('LOCATION')
