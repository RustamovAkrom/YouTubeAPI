import os
import sys

from pathlib import Path

from django.utils.translation import gettext_lazy as _

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = bool(os.getenv("DEBUG"))

ALLOWED_HOSTS = str(os.getenv("ALLOWED_HOSTS")).split(",")

INSTALLED_APPS = [
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
    'apps.shared.apps.SharedConfig',
    'apps.users.apps.UsersConfig',
    'apps.videos.apps.VideosConfig',

    # Third party apps
    'rest_framework',
    'modeltranslation',
    'rosetta',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES_PATH = [os.path.join(BASE_DIR, "templates")]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_PATH,
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DATABASE_NAME"),
#         "USER": os.getenv("DATABASE_USER"),
#         "PASSWORD": os.getenv("DATABASE_PASSWORD"),
#         "HOST": os.getenv("DATABASE_HOST"),
#         "PORT": os.getenv("DATABASE_PORT"),
#         "TEST": {
#             "NAME": "mytestdatabase",
#         }
#     }
# }

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

gettext = lambda s: _(s)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ("en", gettext("English")),
    ("ru", gettext("Russian")),
    ("uz", gettext("Uzbek")),
)

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'ru', 'uz')
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
        },
    },
    'formatters': {
        'utf8': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

CACHES = {
    "default": {
        # "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        # "BACKEND": 'django.core.cache.backends.db.DatabaseCache',
        "BACKEND": 'django.core.cache.backends.filebased.FileBasedCache',
        # "BACKEND": 'django.core.cache.backends.dummy.DummyCache',
        # "BACKEND": 'django.core.cache.backends.locmem.LocMemCache',
        # "BACKEND": 'django.core.cache.backends.memcached.PyMemcacheCache',
        # "BACKEND": 'django.core.cache.backends.memcached.PyLibMCCache',
        # "BACKEND": 'django.core.cache.backends.redis.RedisCache',
        "LOCATION": os.path.join(BASE_DIR, "cache")
    }
}

AUTH_USER_MODEL = "users.User"

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

## Security productions
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True
