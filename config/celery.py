import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Автоматическое обнаружение и регистрация задач в приложении
# app.autodiscover_tasks()
# Дополнительная конфигурация Celery, если необходимо
# Например, настройки брокера сообщений, расписания и т.д.


# Определение рассписания для таска add_number
# app.conf.beat_schedule = {
#     'add_numbers_task': {
#         'task': 'shops.tasks.send_order_notification',
#         'schedule': 30.0, # Выполнение каждые 30 секунд
#         'args': (), # Аргументы для функции add_numbers
#     },
# }


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')