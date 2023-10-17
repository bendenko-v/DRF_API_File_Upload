from celery import shared_task
from files.models import File


@shared_task
def process_uploaded_file() -> None:
    """ Celery task to process uploaded files """
    File.objects.filter(processed=False).update(processed=True)
