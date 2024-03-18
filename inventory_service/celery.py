import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_service.settings')

celery = Celery('inventory_service')

celery.config_from_object('django.conf:settings', namespace='CELERY')

celery.autodiscover_tasks()