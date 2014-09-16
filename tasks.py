__author__ = 'sebastienclaeys'

from celery import task
import mixpanel
from django.conf import settings as conf

mp = mixpanel.Mixpanel(conf.MIXPANEL_TOKEN)

@task
def track_event(user_id, event_name, properties={}):
    mp.track(user_id, event_name, properties)

