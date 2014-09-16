__author__ = 'sebastienclaeys'

from celery import task
import mixpanel

@task
def track_event(user_id, event_name, properties={}):
    print "[AB testing mixpanel event] - %s" % event_name
    from django.conf import settings as conf
    mp = mixpanel.Mixpanel(conf.MIXPANEL_TOKEN)
    mp.track(user_id, event_name, properties)
