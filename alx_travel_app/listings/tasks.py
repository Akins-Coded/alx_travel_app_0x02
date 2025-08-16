# listing/tasks.py
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

print("Celery task 'add' has been defined.")