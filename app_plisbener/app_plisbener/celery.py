from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_plisbener.settings')

app = Celery('app_plisbener')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Autodiscover tasks in the 'convert' app
app.autodiscover_tasks(['convert'])

# Autodiscover tasks in the 'upload' app
app.autodiscover_tasks(['upload'])