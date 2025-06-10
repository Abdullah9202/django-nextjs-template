from .base import *
from decouple import config

print("✅ Loaded settings from dev.py")

DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True  # For production, keep this False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ['http://localhost', 'http://127.0.0.1'] + [config('FRONTEND_URL', default='http://localhost:3000')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DEV_DB_NAME'),
        'USER': config('DEV_DB_USER'),
        'PASSWORD': config('DEV_DB_PASSWORD'),
        'HOST': config('DEV_DB_HOST'),
        'PORT': config('DEV_DB_PORT'),
    }
}
