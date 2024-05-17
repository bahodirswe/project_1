import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import logging

# from .cdn.conf import (
#     AWS_ACCESS_KEY_ID,
#     AWS_SECRET_ACCESS_KEY,
#     AWS_S3_SIGNATURE_VERSION,
#     AWS_ENDPOINT,
#     AWS_STORAGE_BUCKET_NAME,
#     AWS_ENDPOINT_URL,
#     AWS_S3_OBJEKT_PARAMETERS,
#     DEFAULT_FILE_STORAGE,
#     STATICFILES_STORAGE,
# )

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

WEBSITE_URL = os.environ.get('WEBSITE_URL')


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    "storages",
    "rest_framework",
]

LOCAL_APPS = [
    "blog.apps.BlogConfig",
    "user.apps.UserConfig",
]


INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + LOCAL_APPS
    
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CSRF_TRUSTED_ORIGINS = [
#     f"https://www.{WEBSITE_URL}",
#     f"https://{WEBSITE_URL}",
#     "http://127.0.0.1",
#     "http://localhost"
# ]

# CSRF_COOKIE_DOMEIN = WEBSITE_URL
# CSRF_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_HSTS_SECOND = 3600
# SECURE_HSTS_SECOND_SUBDOMEINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_CONTENT_TYPE_NOSNIFF = True

SITE_ID = 1

CORS_ORIGIN_WHITELIST = [

]

CSRF_TRUSTED_ORIGINS = [
   
]

CORS_ALLOWED_ORIGINS = [
   

]



ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',                
                'django.contrib.messages.context_processors.messages',
                'blog.views.trends_all',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.app'

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": os.environ["DBNAME"],
        "USER": os.environ["DBUSER"],
        "PASSWORD": os.environ["DBPASSWORD"],
        "HOST": os.environ["DBHOST"],
        "PORT": os.environ["DBPORT"],
    }
}


# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
#     DATABASES = {
#         "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
#     }




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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_DIR = BASE_DIR / 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

# AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
# AWS_STORAGE_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME 
# AWS_S3_ENDPOINT_URL = AWS_ENDPOINT_URL
# AWS_S3_OBJEKT_PARAMETERS = AWS_S3_OBJEKT_PARAMETERS 
# AWS_LOCATION = AWS_STORAGE_BUCKET_NAME
# AWS_QUERYSTRING_EXPIRE = 5

# STATIC_URL = 'https://%s/%s/' % (AWS_ENDPOINT, AWS_LOCATION)
# MEDIA_URL = 'https://%s/%s/' % (AWS_ENDPOINT, AWS_LOCATION)

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
# MEDIAFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# STATICFILES_STORAGE = STATICFILES_STORAGE
# DEFAULT_FILE_STORAGE = DEFAULT_FILE_STORAGE

# AWS_ENABLED = True
# AWS_S3_SECURE_URLS = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "user.User"

LOGIN_REDIRECT_URL = "blog:home"
LOGIN_URL = "user:sign_in"
LOGOUT_REDIRECT_URL = "blog:home"


LOGGING = {
    "version": 1,
    "disable_existing_longers": False,
    "filters": {
        "require_debug_false":{
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true":{
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formetters": {
        "django.server":{
            "()": "django.utils.log.ServerFormetter",
            "format": "[%(server_time)s]%(messgae)s",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "console_debug_false":{
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
        },
        'django.server': {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "logfile":{
            "class": "logging.FileHandler",
            "filename": "server.log",
        },
    },

    "loggers":{
        "django":{
            "handlers":[
                "console",
                "console_debug_false",
                "logfile",
            ],
            "level": "INFO",
        },
        "django.server":{
            "hendlers": ["django.server"],
            "level": "INFO",
            "propogate": False,
        },
    },
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
