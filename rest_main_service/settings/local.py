from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='123456789')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

# 'django-insecure-l#yw&4^$ar*ou(em2fml#j#y!e0gr52qbb69v7j%r*pl@47+7y'
