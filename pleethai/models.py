from django.db import models

class Word (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    japanese = models.CharField(max_length=127, null=False, blank=False)
    hiragana =  models.CharField(max_length=127, null=False, blank=False)
    roman = models.CharField(max_length=127, null=True, blank=True)
    thai =  models.CharField(max_length=127, null=False, blank=False)
    pronunciation_symbol = models.CharField(max_length=127, null=True, blank=True)
    pronunciation_kana = models.CharField(max_length=127, null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=1)
    english = models.CharField(max_length=127, null=True, blank=True)
    searchs = models.BigIntegerField(default=0)
    wordclass_id = models.ForeignKey("WordClass", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ", " + self.japanese + ", " + self.hiragana+ ", " + self.thai

class WordClass (models.Model): 
    id = models.PositiveSmallIntegerField(primary_key=True)
    thai = models.CharField(max_length=31, null=True, blank=True)
    japanese = models.CharField(max_length=31, null=True, blank=True)
    slug = models.SlugField(max_length=31, null=True, blank=True)

    def __str__(self):
        return self.slug

class Example (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    japanese = japanese = models.CharField(max_length=511, null=False, blank=False)
    hiragana =  models.CharField(max_length=511, null=True, blank=True)
    roman =  models.CharField(max_length=511, null=True, blank=True)
    thai =  models.CharField(max_length=511, null=True, blank=True)
    pronunciation_symbol = models.CharField(max_length=511, null=True, blank=True)
    pronunciation_kana = models.CharField(max_length=511, null=True, blank=True)
    english = models.CharField(max_length=511, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ", " + self.japanese

class Constituent (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    example_id = models.ForeignKey("Example", on_delete=models.PROTECT)
    word_id = models.ForeignKey("Word", on_delete=models.PROTECT)
    order = models.PositiveSmallIntegerField(null=False)

    class Meta:
        unique_together = ("example_id", "word_id", "order")

    def __str__(self):
        return str(self.example_id) + ", " + str(self.word_id) + ", " + str(self.order)




