from .settings import *  # noqa


DEBUG = False
SECRET_KEY = "zvh+vsa)c7$)(z@z7+c!c%ex1k8lqm)*6eh4l#a(t-_m@-i_9&"
SITE_ID = 1

# --- DATABASE ---
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}
