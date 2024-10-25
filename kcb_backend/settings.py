"""
Django settings for kcb_backend project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*vqxoy-w(x4zc6%i&ld(y-_1u708%xu(5m8w=r7nkcn0qy%m5c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Custom Application,
    'kcb_accounts',
    'kcb_settings',
    'kcb_ldms',
    'kcb_report',
    'kcb_uaa',
    

    # Custom Libraries
    'graphene_django',
    'provider',
    'provider.oauth2',
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kcb_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'kcb_backend_html')],
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

WSGI_APPLICATION = 'kcb_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': config['DATABASE_NAME'],
#        'USER': config['DATABASE_USER'],
#        'PASSWORD': config['DATABASE_PASSWORD'],
#        'HOST': config['DATABASE_HOST'],
#        'PORT': config['DATABASE_PORT'],
#    }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/kcb_backend_static/'
MEDIA_ROOT = '/kcb_backend_media/'
STATIC_ROOT = os.path.join(BASE_DIR, "kcb_backend_static") 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CUSTOM SETTINGS

GRAPHENE = {
    'SCHEMA': 'kcb_backend.main_schema.schema'
}


# CORSHEADERS
CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = ["*"]

# CSRF_TRUSTED_ORIGINS = ["*"]

# EMAIL CONFIGURATIONS

# EMAIL_HOST = config['EMAIL_HOST']
# EMAIL_PASSWORD = config['EMAIL_PASSWORD']
# EMAIL_USER = config['EMAIL_USER']
# EMAIL_PORT = config['EMAIL_PORT']
# EMAIL_USE_SSL = config['EMAIL_USE_SSL']
# EMAIL_USE_TLS = config['EMAIL_USE_TLS']
# DEFAULT_FROM_EMAIL = config['DEFAULT_FROM_EMAIL']
# EMAIL_SSL_VERIFICATION = False