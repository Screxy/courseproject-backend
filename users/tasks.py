from celery import shared_task
from django.contrib.auth.models import User
from .services import save_visits_from_cache
from django.core.mail import send_mail, BadHeaderError


@shared_task
def send_email_for_new_user(user_pk):
    print('start')
    user = User.objects.get(pk=user_pk)
    print(f'Sending email to {user.email}')
    try:
        send_mail('CourseProject', f'Welcome to my project {user.first_name}',
                  'admin@admin.com', [user.email], fail_silently=False)
    except BadHeaderError:
        print('Invalid')


@shared_task
def periodic_save_visits():
    save_visits_from_cache()
