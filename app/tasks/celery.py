from celery import Celery

from app.config import settings

celery = Celery("tasks", broker=settings.get_redis_url(), include=["app.tasks.tasks"])
