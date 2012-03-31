from django import template
from django.conf import settings
import hashlib

register = template.Library()

@register.simple_tag
def avatar(user, **kwargs):
    DEFAULT_SIZE = 80
    # other options: 404, mm, monsterid, wavatar, retro
    DEFAULT = 'identicon'

    hash = hashlib.md5(user.email.lower().strip()).hexdigest()
    size = kwargs.get('size', DEFAULT_SIZE)

    return u'{src}?s={size}&d={default}'.format(
        src=settings.GRAVATAR_URI + hash,
        size=size,
        default=DEFAULT)
