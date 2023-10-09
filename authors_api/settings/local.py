from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="OyWppf9OoaXeShGSzka32oEjQ9rNhHLRZgmBLPjMqAeXUwG5vac",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080"
]  # List of domains that are allowed to make cross-site requests to your site.
