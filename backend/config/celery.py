from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')

app = Celery('config')
app.conf.enable_utc = False

app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(slef):
    print(f"Requests: {self.request!r}")

