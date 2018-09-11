"""
Django settings for classroomtools project.

Import from base

"""

from classroomtools.settings.base import *
from decouple import config

#use the config lines below if using configparser with .ini file
#config = configparser.ConfigParser()
#config.read(os.path.join(PROJECT_ROOT, 'config.ini'))

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config['general']['secretkey']



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS += [

]


# setup email
#EMAIL_HOST = config['emailconfig']['emailhost']
#EMAIL_HOST_USER = config['emailconfig']['username']
#EMAIL_HOST_PASSWORD = config['emailconfig']['password']
##EMAIL_HOST = config('EMAIL_HOST')
##EMAIL_HOST_USER = config('EMAIL_USERNAME')
##EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
##EMAIL_USE_TLS = True
##DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
##EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
		'USER': config('DB_USER'),
		'PASSWORD': config('DB_PASSWORD'),
		'HOST': config('DB_HOST'),
		'PORT': config('DB_PORT', cast=int),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# compression and caching support from whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

