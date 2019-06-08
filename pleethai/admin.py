from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from pleethai.models import Word, WordClass, Example, Constituent

# TODO 以下は作成したモデルに従って修正する
class WordResource(resources.ModelResource):

    class Meta:
        model = Word

class WordClassResource(resources.ModelResource):

    class Meta:
        model = WordClass

class ExampleResource(resources.ModelResource):

    class Meta:
        model = Example

class ConstituentResource(resources.ModelResource):

    class Meta:
        model = Constituent

class WordAdmin(ImportExportModelAdmin):
    resource_class = WordResource

class WordClassAdmin(ImportExportModelAdmin):
    resource_class = WordClassResource

class ExampleAdmin(ImportExportModelAdmin):
    resource_class = ExampleResource

class ConstituentAdmin(ImportExportModelAdmin):
    resource_class = ConstituentResource

admin.site.register(Word, WordAdmin)
admin.site.register(WordClass,WordClassAdmin)
admin.site.register(Example, ExampleAdmin)
admin.site.register(Constituent, ConstituentAdmin)
