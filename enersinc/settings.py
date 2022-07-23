
from calendar import TUESDAY
import os
from pathlib import Path
from datetime import timedelta
from urllib.parse import urlparse
from django.core.management.utils  import get_random_secret_key
import dj_database_url
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY',get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG","FALSE") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS","127.0.0.1,localhost").split(",")
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

# Application definition

INSTALLED_APPS = [
   'tasks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
]


REST_FRAMEWORK={
  'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

]


# CORS_ALLOW_ALL_ORIGINS= True

# CORS_ALLOWED_ORIGINS=[
#    "http://localhost:3000",
#    "http://127.0.0.1:3000",
   
# ]


ROOT_URLCONF = 'enersinc.urls'

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

WSGI_APPLICATION = 'enersinc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"



DATABASES={
      "default":{
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "db",
        'USER': "db",
        'PASSWORD':"AVNS_yvwX9QOa_RSOYwhxGLE",
        'HOST': "app-3e1d7f7e-b10f-4bf1-bd3b-c61ce38a6caa-do-user-12082101-0.b.db.ondigitalocean.com",
        'PORT': 25060,
        "OPTIONS" :{"sslmode":"require"}, 
      }
}




# if DEVELOPMENT_MODE is True:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#         }
#     }
# elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
#     if os.getenv("DATABASE_URL", None) is None:
#         raise Exception("DATABASE_URL environment variable not defined")
#     DATABASES = {
#         "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
#     }


# if os.getenv("DATABASE_URL","") != "":
#    r=urlparse(os.environ.get("DATABASE_URL"))
#    DATABASES={
#       "default":{
#          'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.path.relpath(r.path,"/"),
#         'USER': r.username,
#         'PASSWORD':r.password,
#         'HOST': r.hostname,
#         'PORT': r.port,
#         "OPTIONS" :{"sslmode":"require"}, 
#       }
#    }
# else :
#    DATABASES = { 
#       'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'tqccctrx',
#          'USER': 'tqccctrx',
#          'PASSWORD':'ncX2bMZDdUxIwCx1yRm3icg7zZktei_T',
#          'HOST':'rogue.db.elephantsql.com',
#          'PORT': '5432',
#       }
#    }

# PORT = os.getenv("PORT", default="5000")



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/



# STATIC_TMP = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field



# STATICFILES_DIRS =(
#    os.path.join(BASE_DIR,'static'),
# )

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# import django_heroku
# django_heroku.settings(locals())