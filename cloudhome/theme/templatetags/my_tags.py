# In your templatetags/my_tags.py file
from django import template

register = template.Library()

@register.simple_tag
def is_staff(user):
    return user.is_staff