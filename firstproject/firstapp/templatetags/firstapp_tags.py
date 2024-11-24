from django import template
import firstapp.views as views


register = template.Library()


@register.inclusion_tag('firstapp/list_categories.html')
def show_categories():
    cats = views.cats_db
    return {'cats': cats}