from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'files_api.settings')

app = Celery(
    'files_api', broker_connection_retry_on_startup=True
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Add your periodic task
app.conf.beat_schedule = {
    'process-files-every-one-minute': {
        'task': 'files.tasks.process_uploaded_file',
        'schedule': crontab(minute='*/1'),
    },
}

app.conf.timezone = 'UTC'
