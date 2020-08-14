from .common import *


# DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'emholboo',
        'USER': 'emholboouser',
        'PASSWORD': 'emholboopassword',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

