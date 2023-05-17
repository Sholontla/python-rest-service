import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rest_main_service.settings.local')

application = get_wsgi_application()
