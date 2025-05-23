import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0)l8gl3(trzp-gyfmu1kifx3ivv4g=!g_vwr18n=9e*!#4vah^"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = os.getenv(key="DJANGO_ALLOWED_HOSTS", default="127.0.0.1").split(",")


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",

    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "djoser",
]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

CORS_ALLOW_HEADERS = [
    "content-type",
    "dnt",
    "origin",
    "cache-control",
    "x-requested-with",
    "accept-encoding",
    "user-agent",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": f"django.db.backends.{os.getenv(key='DATABASE_ENGINE', default='sqlite3')}",
        "NAME": f"{os.getenv(key='DATABASE_NAME', default='db.sqlite3')}",
        "USER": f"{os.getenv(key='DATABASE_USERNAME', default='dbuser')}",
        "PASSWORD": f"{os.getenv(key='DATABASE_PASSWORD', default='userpass')}",
        "HOST": f"{os.getenv(key='DATABASE_HOST', default='127.0.0.1')}",
        "PORT": f"{os.getenv(key='DATABASE_PORT', default='5432')}",
    },
    "TEST": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}


REST_FRAMEWORK = {
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-ca"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = False


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CORS_ALLOW_ALL_ORIGINS = True

