# -*- coding: utf-8 -*-
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()

@register.filter
def contains(folder, item):
    return folder.items.filter(pk=item.id).exists()
