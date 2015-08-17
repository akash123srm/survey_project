"""
WSGI config for survey_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
from .settings import PROJECT_PATH

if PROJECT_PATH not in sys.path:
    sys.path += PROJECT_PATH
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "survey_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
