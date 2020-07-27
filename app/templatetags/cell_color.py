from django import template


register = template.Library()

@register.filter
def cell_color(val):
    if val:
        val = float(val)
        if val > 50:
            return '#cc0000'
        elif val > 5:
            return 'Red'
        elif val > 2:
            return '#ff6666'
        elif val > 1:
            return '#ff9999'
        elif val < 0:
            return '#00ff99'
        else:
            return 'White'


@register.filter
def dash_empty(val):
    if not val:
        return '-'
    else:
        return val
