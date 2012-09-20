# Django settings for librement project.

from setup_warnings import *

from os.path import join, dirname, abspath

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Raphael Hertzog', 'raphael@freexian.com'),
)

INTERNAL_IPS = ('127.0.0.1',)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'librement',
        'USER': 'librement',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

LIBREMENT_BASE_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/srv/librement/storage/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/storage/'

# Make this unique, and don't share it with anybody.
try:
    with open('/var/lib/librement/key', 'r') as f:
        SECRET_KEY = f.read().strip()
except IOError:
    SECRET_KEY = 'swwG4rLmoCMYkKn46r1bOtZLlnUAXFatwY9pv6pzyysYcssHShzse7WSq'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'librement.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    join(LIBREMENT_BASE_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',

    'debug_toolbar',
    'django_autologin',
    'email_from_template',
    'debug_toolbar_user_panel',
    'south',

    'librement.account',
    'librement.registration',
    'librement.passwords',
    'librement.profile',
    'librement.profile.links',
    'librement.static',
    'librement.utils',
)

AUTHENTICATION_BACKENDS = (
    'librement.account.backends.LibrementBackend',
)

DEBUG_TOOLBAR_CONFIG = {
    'HIDE_DJANGO_SQL': True,
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': False,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar_user_panel.panels.UserPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

STATIC_MEDIA_URL = '/media/%(hash).6s/%(path)s'
STATIC_MEDIA_ROOT = join(LIBREMENT_BASE_PATH, 'media')

STATIC_URL = '/media/_/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'librement.utils.context_processors.settings_context',
)

X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_DOMAIN = '.librement.net'

SESSION_COOKIE_DOMAIN = '.librement.net'
SESSION_COOKIE_HTTPONLY = True

SITE_URL = 'http://librement.net'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

APPEND_SLASH = False

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

EMAIL_HOST = 'localhost'

SERVER_EMAIL = 'librement <noreply@librement.net>'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = '[librement] '

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'librement',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

# http://south.aeracode.org/docs/settings.html#south-tests-migrate
SOUTH_TESTS_MIGRATE = False

DATABASE_ENGINE = 'dummy_for_debug_toolbar'

XHR_SIMULATED_DELAY = 0
