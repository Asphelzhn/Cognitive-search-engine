import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'detecht_backend.settings'
django.setup()


def initialize_django():
    return 1
