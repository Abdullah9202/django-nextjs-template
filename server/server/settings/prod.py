from decouple import config
from .base import *

DEBUG = False

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS').split(",")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}