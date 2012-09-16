from django import template

from ..urls import static_media_url

register = template.Library()

@register.simple_tag
def static(url):
    return static_media_url(url)
