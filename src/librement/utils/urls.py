from django.conf import settings

from librement.settings.hashes import HASHES

def static_media_url(path):
    return settings.STATIC_MEDIA_URL % {
        'path': path,
        'hash': HASHES.get(path, '-'),
    }
