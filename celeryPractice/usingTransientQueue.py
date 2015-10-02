from kombu import Exchange, Queue

CELERY_QUEUES = (
    Queue('celery', routing_key='celery'),
    Queue('transient', routing_key='transient',
          delivery_mode=1),
)

