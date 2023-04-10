import os

from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')

app = Celery('management')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.loader.override_backends['django-db'] = 'django_celery_results.backends.database:DatabaseBackend'

#celery beat settings
app.conf.beat_schedule={
    'audit-level-battery-3':{
    'task':'core.tasks.StatusBattery',
    'schedule': crontab(minute='*/3'),
    
    }

}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')