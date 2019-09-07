# Settings that are unique to production go here
from .base import *  # noqa

DEBUG = False

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

CORS_ORIGIN_WHITELIST = [
    "https://young-beyond-25001.herokuapp.com/"
]

