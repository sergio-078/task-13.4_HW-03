import logging
import os
from pathlib import Path

# from decouple import config
logger = logging.getLogger('django')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$u(!)7w#9hq$nc+j(^w@b-ims90re$d0fi3a*ti6db)vnclyfe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',

    'celery',

    'post',
    'accounts',

    'debug_toolbar',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # debug toolbar middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'newsportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'newsportal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# перенаправление пользоввателя после аутентификации
LOGIN_REDIRECT_URL = "/"
# перенаправление пользоввателя после выхода с личного кабинета
LOGOUT_REDIRECT_URL = "/"


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

]


# для работы через модуль allauth

ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# ACCOUNT_CONFIRM_EMAIL_ON_GET = True    # позволяет избежать дополнительного входа и активирует аккаунт сразу, как только мы перейдём по ссылке
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1    # хранит количество дней, когда доступна ссылка на подтверждение регистрации

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}


SITE_URL = 'http://127.0.0.1:8000'


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "newsportal@newsportal.ru"
EMAIL_HOST_PASSWORD = "1111"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "newsportal@newsportal.ru"

SERVER_EMAIL = "newsportal@newsportal.ru"

MANAGERS = (
    ('Ivan', 'ivan@yandex.ru'),
    ('Petr', 'petr@yandex.ru'),
)

ADMINS = (
    ('anton', 'anton@yandex.ru'),
)


APPSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'    # 'Y-m-d H:i:s'
APPSCHEDULER_RUN_NOW_TIMEOUT = 25


CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# BROKER_CONNECTION_RETRY_ON_STARTUP = True


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),  #  Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    },
}


INTERNAL_IPS = [
    # ...
    '127.0.0.1',  # Add your development machine's IP address here
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',

    # форматер - формат записи сообщений
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        'warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        'error_and_critical': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',

        },
        'general_': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        'errors_': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
        'email_': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': '%d.%m.%Y %H-%M-%S',
        },
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning',
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_and_critical',
        },
        'general_log': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'formatter': 'general_',
        },
        'errors_log': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'formatter': 'errors_',
        },
        'security_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/security.log',
            'formatter': 'general_',
        },
        'email': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'email_',
        },
    },
    # регистраторы
    'loggers': {
        'django': {
            'level': 'DEBUG',  # добавляем, чтобы попадало с уровня DEBUG (по умолчанию уровень - INFO)
            'handlers': ['console_debug', 'console_warning', 'console_error', 'general_log'],
            'propagate': True,
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['errors_log', 'email'],
            'propagate': True,
        },
        'django.server': {
            'level': 'ERROR',
            'handlers': ['errors_log', 'email'],
            'propagate': True,
        },
        'django.template': {
            'level': 'ERROR',
            'handlers': ['errors_log'],
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['errors_log'],
            'propagate': True,
        },
        'django.security': {
            'level': 'INFO',      # по умолчанию Warning
            'handlers': ['security_log'],
            'propagate': True,
        },
    },
}