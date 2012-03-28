from django import template
from django.conf import settings
import hashlib

register = template.Library()

@register.simple_tag
def avatar(user):

	hash = hashlib.md5(user.email.lower().strip()).hexdigest()

	return u'<img src="{src}">'.format(src=settings.GRAVATAR_URI + hash)
