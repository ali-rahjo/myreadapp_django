from django import template

# Singleton
# meaning, each time you add a filter, you need to 
# restart your server
register = template.Library()

@register.filter
def semi_colon_separator(value):
    return value.replace(', ', '; ')

@register.filter
def join_fields(values):
    return ', '.join(str(value) for value in values)
