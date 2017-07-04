from django import template
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.inclusion_tag('profile/link.html')
def any_function(model_obj):
    return {"object": model_obj}
