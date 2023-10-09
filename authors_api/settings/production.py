from .base import *  # noqa
from .base import env

ADMINS = [
    ("Zvonimir Horvat", "zochhe@gmail.com")
]  # django will email this person the details of exceptions in req or res in production

# TODO add domain names of the production server

CSRF_TRUSTED_ORIGINS = [""]
# List of domains that are allowed to make cross-site requests to your site.
