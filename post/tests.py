# from django.test import TestCase
import datetime
# from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from newsportal import settings
from post.models import Post


# Create your tests here.
def email_weekly_post_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week).order_by('-dateCreation')
    categories = []
    subscribers = []
    for post in posts:
        categories += [cat for cat in post.category.all()]
    for category in categories:
        subscribers += [sub for sub in category.subscribers.all()]
    print(categories)
    print(subscribers)
    # for subscriber in subscribers:
    #     subject = 'Статьи за неделю!!!',
    #     text_content = render_to_string(
    #         'post/email_weekly_post.html',
    #         {
    #             'username': subscriber.username,
    #             'link': settings.SITE_URL,
    #             'posts': posts,
    #         }
    #     )
    #     html_content = render_to_string(
    #         'post/email_weekly_post.html',
    #         {
    #             'link': settings.SITE_URL,
    #             'posts': posts,
    #         }
    #     )
        # msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [subscriber.email])
        # msg.attach_alternative(html_content, 'text/html')
        # msg.send()
        #
        # print(subscriber.email)
        # print(subscriber.username)

email_weekly_post_task()
