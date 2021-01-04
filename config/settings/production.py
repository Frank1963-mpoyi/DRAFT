import dj_database_url
import django_heroku
from decouple             import config
import configparser
from .base import * # here we import all and we will override the default settings




DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'mpoyitshibuyi.herokuapp.com']


DATABASES['default'] =  dj_database_url.config()






MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT  =   os.path.join(BASE_DIR, 'staticfiles')


# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



CORPS_REPLACE_HTTPS_REFERER     = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True


prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
django_heroku.settings(locals())

ENVIRONMENT = 'PRODUCTION'

print("\n")
print("DEBUG        = ", DEBUG)
print("MODE         = ", ENVIRONMENT)
print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT)
print("\n")

