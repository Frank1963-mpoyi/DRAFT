import configparser
from .base import *


DEBUG = True

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1'
]

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

#DATABASE_ROUTERS = ['config.router.AuthRouter']

CONFIG_DIR = os.path.join(BASE_DIR, 'config/')

parser = configparser.ConfigParser()
parser.read_file(open(os.path.join(CONFIG_DIR, 'app.ini')))


# Done with postgresql 
DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql',
        'NAME'      : parser.get('Draft', 'name'),
        'USER'      : parser.get('Draft', 'user'),
        'PASSWORD'  : parser.get('Draft', 'password'),
        'HOST'      : parser.get('Draft', 'host') or '127.0.0.1',
        'PORT'      : parser.getint('Draft', 'port') or '5432',

    }
}


# DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True


CORPS_REPLACE_HTTPS_REFERER     =False
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_HSTS_SECONDS             = None
SECURE_FRAME_DENY               = False


ENVIRONMENT = 'DEVELOPMENT'

print("\n")
print("DEBUG        = ", DEBUG)
print("MODE         = ", ENVIRONMENT)
print("TEMPLATES    = ", TEMPLATES[0]['DIRS'])
print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT)
print("\n")
