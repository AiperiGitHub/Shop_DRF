from pathlib import Path
from config.settings import BASE_DIR

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0m3nyqx+ehmub0b+tws%ppbe!v1&)v)q3@e@f^3)80_7%!bysb'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
