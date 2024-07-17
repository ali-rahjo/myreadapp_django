from django import template

# Singleton
# meaning, each time you add a filter, you need to 
# restart your server
register = template.Library()

@register.filter
def semi_colon_separator(value):
    return value.replace(', ', '; ')
