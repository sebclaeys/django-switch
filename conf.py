from django.conf import settings

PRELOAD_SWITCHES = getattr(settings, 'PRELOAD_SWITCHES', False)
