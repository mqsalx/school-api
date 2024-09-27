# setup\settings\databases.py

import os

from dotenv import load_dotenv

load_dotenv()

if os.environ.get("ENV_MODE") == "development":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DATABASE_ENGINE"),
            "NAME": os.environ.get("DATABASE_NAME"),
            "USER": os.environ.get("DATABASE_USER"),
            "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
            "HOST": os.environ.get("DATABASE_HOST"),
            "PORT": os.environ.get("DATABASE_PORT"),
        }
    }
