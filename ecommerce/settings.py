
import os
import dj_database_url
from pathlib import Path
from django.contrib.messages import constants as messages
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import environ 

env=environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$nldih*0%11h5y4qai&l^kzqgu8#d_6uuihs*hwy51^l)@tln3"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1","localhost","innovatechapp.onrender.com"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "category",
    "accounts",
    "store",
    "carts",
    "orders",
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
      'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "category.context_processors.menu_links",
                "carts.context_processors.counter",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce.wsgi.application"
AUTH_USER_MODEL='accounts.Account'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
# 	'default': {
# 		'ENGINE':'django.db.backends.postgresql_psycopg2',
# 		'NAME':'tech_db',
# 		'USER':'postgres',
# 		'PASSWORD':'fadeM3',
# 		'HOST':'localhost', 
# 		'PORT':'5432' 
# 	}
# }

# Configuración para utilizar DATABASE_URL si está definida en las variables de entorno.
# Don't forget to import dj-database-url at the beginning of the file

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.config(
#         # Feel free to alter this value to suit your needs.
#         default='postgres://postgres:fadeM3@localhost:5432/tech_db',
#         conn_max_age=600
#     )
# }
        # default='postgres://tech_t0jz_user:8Rj9mZlcgCpxs3rZ7wriUM2DGXg63ZU9@dpg-cmu90hvqd2ns738h3fmg-a.oregon-postgres.render.com/tech_t0jz',

if 'RENDER_EXTERNAL_HOSTNAME' in os.environ:
    # Configuración para Render
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('RENDER_DB_NAME'),
            'USER': os.environ.get('RENDER_DB_USER'),
            'PASSWORD': os.environ.get('RENDER_DB_PASSWORD'),
            'HOST': os.environ.get('RENDER_DB_HOST'),
            'PORT': os.environ.get('RENDER_DB_PORT', ''),
            'CONN_MAX_AGE': 600,
            'CONN_HEALTH_CHECKS': False,
        }
    }
else:
    # Configuración para entorno local
   DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': 'tech_db',
        'USER': 'postgres',
        'PASSWORD':'fadeM3',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

    

# Obtener la URL de la base de datos directamente
# print("DATABASE URL:",  database_config)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT=BASE_DIR/'static'
# STATICFILES_DIRS = [
#     'ecommerce/static'
# ]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL="/media/"
MEDIA_ROOT=BASE_DIR/"media"

MESSAGE_TAGS = {

    messages.ERROR: 'danger',
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587 # 26 para TLS desactivado o 465 para TLS activado
EMAIL_HOST_USER="innovatech71@gmail.com"
EMAIL_HOST_PASSWORD="pifr zmug eyzo fpjc"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
