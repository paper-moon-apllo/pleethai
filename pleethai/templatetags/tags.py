from django import template
from pleethai.models import SysWordThai, Constituent, Tag, TaggedItem
register = template.Library()

# Custom template tag for get thai list 
@register.filter(name='get_thai_list')
def get_thai_list(value):
    return SysWordThai.objects.filter(japanese_id=value).order_by('order')

# Custom template tag for get tag list
@register.filter(name='get_tag_list')
def get_tag_list(value):
    id_list =  Constituent.objects.filter(example_id=value).select_related('japanese_id') \
        .values_list('word_id__tags').distinct()
    return Tag.objects.filter(id__in=id_list).order_by('id')
