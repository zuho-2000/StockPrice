from django import template
 
 
register = template.Library()
 
@register.filter(name="unit_price")
def multipliy(price, volume):
    return round(price / volume,2)