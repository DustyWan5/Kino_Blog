import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kino_blog_project.settings')

app = Celery('kino_blog_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
