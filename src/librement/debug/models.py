from debug_toolbar.middleware import DebugToolbarMiddleware

from django.conf import settings

DebugToolbarMiddleware._show_toolbar = lambda *x: settings.DEBUG
