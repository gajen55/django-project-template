from {{ project_name }}.settings.staging import *

# There should be only minor differences from staging

DATABASES['default']['NAME'] = '{{ project_name }}_production'
DATABASES['default']['USER'] = '{{ project_name }}_production'

EMAIL_SUBJECT_PREFIX = '[{{ project_name|title }} Prod] '

# Uncomment if using celery worker configuration
# BROKER_URL = 'amqp://{{ project_name }}_production:%s@127.0.0.1:5672/{{ project_name }}_production' % os.environ['BROKER_PASSWORD']
