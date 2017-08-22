from django.dispatch import receiver
from .signals import *

@receiver(post_saved)
def send_notification_on_tweet(sender, **kwargs):
	""" To send notification to user's friends for new post """
	print 'send notification'

