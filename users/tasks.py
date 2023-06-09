import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import CustomUser, EmailVerification


@shared_task
def send_email_verification(user_id):
    user = CustomUser.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), expiration=expiration, user=user)
    record.send_verification_email()
