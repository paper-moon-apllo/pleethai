from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from pleethai.models import Word, SysWordJapanese, SysWordThai, WordClass, Example, Constituent
from pleethai.common import Common
from django.conf.urls import url
from django.contrib import messages
from django.shortcuts import redirect

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
    # Add "UPDATE SYS_WORD TABLES" button
    change_list_template = "admin/pleethai/Word/change_list.html"

    # URL for update system tables
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'^updatesystables/$', self.admin_site.admin_view(self.updatesystables)),
        ]
        return my_urls + urls

    # Condition of search
    def existJapanese(self, sys_ja: SysWordJapanese, word: Word) -> bool:
        if not isinstance(sys_ja, SysWordJapanese) or not isinstance(word, Word):
            return False
        return sys_ja.japanese == word.japanese and sys_ja.hiragana == word.hiragana

    # Create Sys_word_Japanse table and Sys_Word_Thai table from Word table
    def updatesystables(self, request):
        all_words = Word.objects.all()
        sys_japanese = []
        sys_thai = []
        try:
            for word in all_words:
                # If there is not word in sys_japanese, add japanese to Sys_Word_Japanese table
                if not Common.contains(sys_japanese, word, self.existJapanese):
                    sys_japanese.append(SysWordJapanese.create(word))
                # Add thai to Sys_Word_Thai table
                tempThai = SysWordThai.create(word, sys_japanese)
                if tempThai != None:
                    sys_thai.append(tempThai)
            # delete and recreate
            SysWordThai.objects.all().delete()
            SysWordJapanese.objects.all().delete()
            SysWordJapanese.objects.bulk_create(sys_japanese)
            SysWordThai.objects.bulk_create(sys_thai)
            messages.info(request, "Succeeded to update system tables")
        except Exception as e:
            messages.error(request, "Failed to update system tables")
            messages.error(request, str(e))
        return redirect(request.META['HTTP_REFERER'])        

class WordClassAdmin(ImportExportModelAdmin):
    resource_class = WordClassResource

class ExampleAdmin(ImportExportModelAdmin):
    resource_class = ExampleResource

class ConstituentAdmin(ImportExportModelAdmin):
    resource_class = ConstituentResource

admin.site.register(Word, WordAdmin)
admin.site.register(SysWordJapanese)
admin.site.register(SysWordThai)
admin.site.register(WordClass,WordClassAdmin)
admin.site.register(Example, ExampleAdmin)
admin.site.register(Constituent, ConstituentAdmin)
