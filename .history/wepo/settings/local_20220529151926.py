from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': con
    }
}