"""
Django settings for detail_shop project.

Generated by 'django-admin_panel startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    "debug_toolbar",
    'webapp',
    'accounts',
    'carts',
    'orders',
    'part',
    'admin_panel'
    'lang',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'detail_shop.urls'

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

WSGI_APPLICATION = 'detail_shop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str("NAME"),
        'USER': env.str("USER"),
        'PASSWORD': env.str("PASSWORD"),
        'HOST': env.str("HOST"),
        'PORT': env.int("PORT"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "cache",
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
# #     {
# #     #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# #     # # },
# #     # # {
# #     # #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# #     # # },
# #     # # {
# #     # #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# #     # # },
# #     # # {
# #     # #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
# #     # # },
# # ]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGES = [
    ('ru', 'Russian'),
    ('en', 'English'),
    ('ko', 'Korean'),
]

LANGUAGE_CODE = 'ru'

TELEGRAM_BOT_TOKEN = '7751663655:AAH_LSqPA1KLRCuEMDsLl_8s-QkaGZndbw4'
TELEGRAM_CHAT_ID = ('1463061700')

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/parts/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
MEDIA_URL = 'parts/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

LOGOUT_REDIRECT_URL = '/'
