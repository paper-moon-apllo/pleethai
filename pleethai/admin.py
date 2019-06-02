from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
#from pleethai.models import SampleModel ※要置換

# TODO 以下は作成したモデルに従って修正する
# class SampleModelResource(resources.ModelResource):

#     class Meta:
#         model = SampleModel
#         fields = ('id', 'name', 'sex',)

# @admin.register(SampleModel)
# class SampleModelAdmin(ImportExportModelAdmin):
#     resource_class = SampleModelResource


    
