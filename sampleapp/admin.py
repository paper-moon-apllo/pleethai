from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from sampleapp.models import SampleModel


class SampleModelResource(resources.ModelResource):

    class Meta:
        model = SampleModel
        fields = ('id', 'name', 'sex',)

@admin.register(SampleModel)
class SampleModelAdmin(ImportExportModelAdmin):
    resource_class = SampleModelResource


    
