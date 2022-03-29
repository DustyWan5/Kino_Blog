from django.core.mail import send_mail
from kino_blog_project.celery import app


@app.task
def send_activation_email(email, activation_code):
    activation_url = f'http://localhost:8000/api/v1/account/activate/{activation_code}/'
    message = f'''
                Thank you for signing up.
                Please, activate your account and subscribe to our online cinema
                Activation link: {activation_url}
                '''
    send_mail(
        'Activate your account and subscription',
        message,
        'test@online_cinema.kg',
        [email, ],
        fail_silently=False
    )
