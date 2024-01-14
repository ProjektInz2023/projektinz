# import os
# from system_zamowien.settings import *
# from system_zamowien.settings import BASE_DIR

# ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
# CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']]
# DEBUG = False

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# from system_zamowien.config import DB_NAME, DB_PASSWORD, DB_URL, DB_USER, DB_PORT

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': DB_NAME,
#         'USER': DB_USER,
#         'PASSWORD': DB_PASSWORD,
#         'HOST': DB_URL,
#         'PORT': DB_PORT,
#         'OPTIONS': {
#                 'driver': 'ODBC Driver 18 for SQL Server',
#             },
#     }
# }
