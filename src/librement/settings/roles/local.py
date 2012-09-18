from os.path import join, dirname, abspath

def base_dir(*paths):
    return join(
        dirname(dirname(dirname(dirname(abspath(__file__))))),
        *paths
    )

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'librement.sqlite',
    },
}

CSRF_COOKIE_DOMAIN = None
SESSION_COOKIE_DOMAIN = None

MEDIA_ROOT = base_dir('storage')
STATIC_MEDIA_URL = '/media/%(path)s'

SITE_URL = 'http://127.0.0.1:8000'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
