import hashlib
import feedparser

from django.core.cache import cache

def get_rss_feed(url):
    if not url:
        return None

    key = 'feed:%s' % hashlib.sha1(url).hexdigest()
    feed = cache.get(key)

    if feed is None:
        feed = feedparser.parse(url)
        cache.set(key, feed, 3600)

    return feed
