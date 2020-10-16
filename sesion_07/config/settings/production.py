"""Production configuration"""

from .base import *

import os

import dj_database_url


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG') or False
ALLOWED_HOSTS = [
    'bedu-movies-django.herokuapp.com',
    'django-env.eba-gvdbmmkk.us-west-2.elasticbeanstalk.com',
]

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Database

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

DATABASES['default']['ATOMIC_REQUESTS'] = True


# Whitenoise
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
