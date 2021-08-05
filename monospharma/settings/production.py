# -*- coding:utf-8 -*-

"""
Production settings
"""

from .common import *

DEBUG = True
ALLOWED_HOSTS = [
    "10.0.0.153",
    "localhost",
    "127.0.0.1",
    "www.monospharma.mn",
    "monospharma.mn",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mnpharma",
        "USER": "mnpharmauser",
        "PASSWORD": "mnpharmauser",
        "HOST": "10.0.0.153",
        "PORT": "5432",
    }
}

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": "debug.log",
#         },
#     },
#     "loggers": {
#         "django": {"handlers": ["file"], "level": "DEBUG", "propagate": True, },
#     },
# }
