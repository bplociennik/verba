from datetime import timedelta

import environ


env = environ.Env()
root = environ.Path(__file__) - 2
BASE_DIR = root()
DEBUG = env("DEBUG", default=False)
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
SITE_ID = env("SITE_ID", default=1)
ROOT_URLCONF = "src.config.urls"
WSGI_APPLICATION = "config.wsgi.application"
AUTH_USER_MODEL = "users.User"

# --- SUPERUSER ---
POPULATE_SUPERUSER = env.bool("POPULATE_SUPERUSER", default=False)
SUPERUSER_EMAIL = env("SUPERUSER_EMAIL")
SUPERUSER_PASSWORD = env("SUPERUSER_PASSWORD")

# --- INSTALLED APPS ---
LOCAL_APPS = (
    "config",
    "users",
    "words",
    "sentences",
)

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "corsheaders",
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",
    "dj_rest_auth",
) + LOCAL_APPS


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- WERKZEUG ---
RUNSERVERPLUS_POLLER_RELOADER_TYPE = env(
    "RUNSERVERPLUS_POLLER_RELOADER_TYPE", default="watchdog"
)

# --- TEMPLATES ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [root("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --- REST FRAMEWORK ---
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_RENDER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.utils.JWTCookieAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 25,
    "NON_FIELD_ERRORS_KEY": "errors",
}

# --- AUTH ---
REST_USE_JWT = True
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# --- CORS ---
CORS_ORIGIN_ALLOW_ALL = env.bool("CORS_ORIGIN_ALLOW_ALL", default=False)
CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST", default=[])

# --- DATABASE ---
DATABASES = {
    "default": env.db(default="postgres://postgres:postgres@postgres:5432/postgres")
}

# --- CELERY ---
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://redis:6379/2")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="redis://redis:6379/3")
CEKERY_DEFAULT_QUEUE = env("CEKERY_DEFAULT_QUEUE", default="default")
CELERY_BEAT_SCHEDULE = {}

# --- CACHALOT ---
CACHALOT_ENABLED = env.bool("CACHALOT_ENABLED", default=not DEBUG)

# --- CACHE ---
CACHES = {
    "default": env.cache(
        default="redis://redis:6379/1?client_class=django_redis.client.DefaultClient"
    )
}

# --- EMAIL ---
if env.bool("SMTP_EMAIL_CONSOLE", default=False):
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_HOST_USERNAME = env("EMAIL_HOST_USERNAME", default="")
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="")

# --- DEBUG TOOLBAR ---
ENABLE_DEBUG_TOOLBAR = env.bool("ENABLE_DEBUG_TOOLBAR", default=DEBUG)
if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_COLLAPSED": True,
        "SHOW_TOOLBAR_CALLBACK": lambda _: True,
    }

# --- ADMIN ---
LOGIN_REDIRECT_URL = "/admin"

# --- STATIC FILES ---
STATIC_URL = "/static/"
STATIC_ROOT = env("STATIC_ROOT", default="/code/static")
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
MEDIA_URL = "/media/"
MEDIA_ROOT = env("MEDIA_ROOT", default="/code/media")

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---  INTERNALIZATION ---
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
