from celery import shared_task
from django.core.mail import send_mail
from apps.users.models import User


@shared_task
def send_email_task(to_emails, from_email, subject, message):
    try:
        send_mail(
            subject=subject, 
            message=message, 
            from_email=from_email, 
            recipient_list=to_emails, 
            fail_silently=False
        )
    except Exception as e:
        print("Email sent error: " + e)
