from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#SESSION_COOKIE_SECURE = False
#CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ognuj2_(paaj+d!(+q7qxwsjkon=ang^&abp!@m9ly(%qva(!f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*', 'https://kind-forest-09e09e903.4.azurestaticapps.net/', 'https://34.118.43.161:8080']

AUTH_USER_MODEL = 'api.Staff'


# Application definition


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=180),
    'ROTATE_REFRESH_TOKENS': False,
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.MyTokenObtainPairSerializer",
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
}

CORS_ALLOWED_ORIGINS = [
    "https://192.168.0.69:8080",
    "https://192.168.0.69:8081",
    "https://kind-forest-09e09e903.4.azurestaticapps.net",
    "https://34.118.43.161:8080",
]

#CORS_ALLOW_ALL_ORIGINS = True
#CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://192.168.0.69:8080",
    "https://192.168.0.69:8081",
    "https://kind-forest-09e09e903.4.azurestaticapps.net/",
    "https://34.118.43.161:8080",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'system_zamowien.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates/')],
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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

WSGI_APPLICATION = 'system_zamowien.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

from system_zamowien.config import DB_NAME, DB_PASSWORD, DB_URL, DB_USER, DB_PORT

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "postgres",
        'USER': "postgres",
        'PASSWORD': "postgres",
        'HOST': "kantyna.c5dhgq0j5peq.eu-north-1.rds.amazonaws.com",
        'PORT': 5432,
    }
}


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

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

STRIPE_PUBLIC_KEY = "pk_test_51OVeTkA8AWLRKBxKwmMaoJSa6mIZoALPETb8RmcsbLJpB1PPefhIX9xqHiMiIX6MuxQunfKLerzcwWtVsRLwSMVz000aZTLhJE"
STRIPE_SECRET_KEY = "sk_test_51OVeTkA8AWLRKBxKPIBbrNgXbgSWZ4pcs3shNxtaB6c7pgYsKfc5g9FUcZvRqGpPybtRRDiJCmxqkYJq61NgYb1700bn8y3Pel"
STRIPE_WEBHOOK_SECRET = ""
