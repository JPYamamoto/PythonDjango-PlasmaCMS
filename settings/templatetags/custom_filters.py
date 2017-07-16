from django import template
from django.core.files.storage import default_storage


def file_exists(file):
    if default_storage.exists(file):
        return True
    return False

register = template.Library()
register.filter('file_exists', file_exists)
