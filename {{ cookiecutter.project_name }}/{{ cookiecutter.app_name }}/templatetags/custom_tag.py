from django import template
register = template.Library()

@register.filter
def get_key(mapping, key):
    return mapping.get(key, '')


@register.filter
def url(element):
    return element.replace(" ","-")