import os


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME": (
            os.environ.get("DATABASE_NAME_DEV")
            if os.environ.get("ENV_MODE") == "development"
            else os.environ.get("DATABASE_NAME_PROD")
        ),
        "USER": (
            os.environ.get("DATABASE_USER_DEV")
            if os.environ.get("ENV_MODE") == "development"
            else os.environ.get("DATABASE_USER_PROD")
        ),
        "PASSWORD": (
            os.environ.get("DATABASE_PASSWORD_DEV")
            if os.environ.get("ENV_MODE") == "development"
            else os.environ.get("DATABASE_PASSWORD_PROD")
        ),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    }
}
