# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config
from dj_database_url import parse as db_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'djamin',
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'sfd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sfd.wsgi.application'


# Database

DATABASES = {
    'default': db_url(config('DATABASE_URL'))
}


# Internationalization

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media/static'),
)

# Amazon S3 settings

if config('USE_S3', cast=bool):
    AWS_ACCESS_KEY_ID = config('S3_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = config('S3_SECRET_KEY')
    AWS_STORAGE_BUCKET_NAME = config('S3_BUCKET_NAME')
    DEFAULT_FILE_STORAGE = 'sfd.custom_storages.MediaS3BotoStorage'
    STATICFILES_STORAGE = 'sfd.custom_storages.StaticS3BotoStorage'
    S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATIC_URL = S3_URL + '/static/'

    MEDIA_URL = S3_URL + '/media/'
