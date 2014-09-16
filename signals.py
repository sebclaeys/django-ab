__author__ = 'sebastienclaeys'

from django.dispatch import receiver
import django.dispatch as dispatcher

import ab.tasks as task_queue

experiment_impression = dispatcher.Signal(providing_args=["request", "test"])
experiment_converted = dispatcher.Signal(providing_args=["request", "test"])

@receiver(experiment_impression)
def on_experiment_impression(sender, **kwargs):
    task_queue.track_event.delay(kwargs['request'].user.id,
                                 kwargs['test'].experiment.name,
                                 {'type': 'impression',
                                  'template': kwargs['test'].template_name
                                 }
    )

@receiver(experiment_converted)
def on_experiment_converted(sender, **kwargs):
    task_queue.track_event.delay(kwargs['request'].user.id,
                                 kwargs['test'].experiment.name,
                                 {'type': 'conversion',
                                  'template': kwargs['test'].template_name}
    )
