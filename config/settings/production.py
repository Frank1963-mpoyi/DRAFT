import dj_database_url
from .base import *
import cloudinary
import cloudinary.uploader
import cloudinary.api



DEBUG = config('DEBUG', cast=bool)


ALLOWED_HOSTS = ['127.0.0.1', 'mpoyitshibuyi.herokuapp.com']







# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'assets')

STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL='/media/' 
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')# for production 

# #CRISPY_TEMPLATE_PACK ='bootstrap4'
# #LOGIN_REDIRECT_URL = 'home_view' 
# #LOGIN_URL ='login' 


# # Internal Ip for Debug tool bar
# # INTERNAL_IPS = ['127.0.0.1']
# # if not DEBUG:
# #     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# #     EMAIL_HOST_USER = 'frankmpoyi63@gmail.com' 
# #     EMAIL_HOST = 'smtp.gmail.com'
# #     EMAIL_PORT = 587
# #     EMAIL_USE_TLS = True
# #     EMAIL_HOST_PASSWORD = 'Paulin63@mpoyi' 

# # else:
# #     EMAIL_BACKEND = (
# #         "django.co



cloudinary.config( 
    cloud_name = "mpoyi", 
    api_key = "343996562826747", 
    api_secret = "drhcfy7eRgIHUjCw6Dch56-uzH8" 
)


CORPS_REPLACE_HTTPS_REFERER     = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         =
('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True


prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

