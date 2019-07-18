from django import template
from pleethai.models import SysWordJapanese, SysWordThai, Example, Constituent, Tag, TaggedItem
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

# Custom template tag for get example list
@register.filter(name='get_example_list')
def get_example_list(value):
    id_list =  Constituent.objects.filter(word_id=value).values_list('example_id').distinct()
    return Example.objects.filter(id__in=id_list).order_by('id')

# Custom template tag for get constituent list
@register.filter(name='get_const_list')
def get_const_list(value):
    return Constituent.objects.filter(example_id=value).select_related('word_id').order_by('order')

# Custom template tag for get first thai
@register.filter(name='get_first_thai')
def get_first_thai(value):
    return SysWordThai.objects.filter(japanese_id=value).order_by('order').first()