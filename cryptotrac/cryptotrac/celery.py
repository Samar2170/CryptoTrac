from __future__ import absolute_import
from datetime import timedelta
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptotrac.settings')
app=Celery('cryptotrac')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    return 'Request: {0!r}'.format(self.request)


app.conf.update(
    CELERY_BEAT_SCHEDULE={
        'fetch_price': {
            'task': 'core.tasks.fetch_price',
            'schedule': timedelta(seconds=30),
        },
    }
)
