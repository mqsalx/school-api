import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "INSECURE")

ROOT_URLCONF = "setup.urls"

WSGI_APPLICATION = "setup.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

APPEND_SLASH = True

if os.environ.get("ENV_MODE") == "development":
    DEBUG = True
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8042",
        "http://127.0.0.1:8042",
    ]
else:
    DEBUG = False
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
