"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&*b%yee(5maoi_z%f04kw0c!ayjo9d2msd+(fk9s&n3v+!bt#8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'djoser',
    'customer',
    'contest',
    'rest_framework',
    'rest_framework_simplejwt',
    'video_encoding',
    'djcelery',
    'djrill',
    'celery',
    'django_celery_beat',
    'django_celery_results',
    'django_extensions'
]

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_EMAIL_FIELD = 'email'
AUTH_USER_MODEL = 'customer.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

CORS_ORIGIN_ALLOW_ALL = True

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'clouddb2',
        'USER': 'postgres',
        'PASSWORD': 'Pass123.',
        'HOST': 'clouddb2.clkdmbaalecd.us-east-1.rds.amazonaws.com',
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
MEDIA_URL = '/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'medias')

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = "/var/www/example.com/static/"


VIDEO_ENCODING_FORMATS = {
    'FFmpeg': [
        {
            'name': 'mp4_sd',
            'extension': 'mp4',
            'params': [
                '-codec:v', 'libx264', '-crf', '20', '-preset', 'medium',
                '-b:v', '1000k', '-maxrate', '1000k', '-bufsize', '2000k',
                '-vf', 'scale=-2:480',
                '-codec:a', 'aac', '-b:a', '128k', '-strict', '-2',
            ],
        },
    ]
}

# -- Celery
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_PERSISTENT = True
CELERY_DEFAULT_DELIVERY_MODE = 'persistent'
CELERYBEAT_SCHEDULE = {
    "runs-every-30-seconds": {
        "task": "contest.tasks.convert_videos",
        "schedule": timedelta(seconds=120),
        "args": ()
    },
    "runs-every-31-seconds": {
        "task": "contest.tasks.check_videos",
        "schedule": timedelta(seconds=30),
        "args": ()
    },
}
RABBIT_IP = os.environ.get('RABBIT_IP')
RABBIT_PORT = os.environ.get('RABBIT_PORT')
AMQP_HOST = '%s:%s' % (RABBIT_IP, RABBIT_PORT)
BROKER_URL = 'amqp://guest:guest@rabbit//'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'arquimisog3@gmail.com'
EMAIL_HOST_PASSWORD = 'Pass123.'
FRONT_URL = "http://localhost:4200/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')