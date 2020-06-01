from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sentences.models import Sentence

from .models import Word


class WordSentenceInlineAdmin(admin.TabularInline):
    model = Sentence


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    inlines = (WordSentenceInlineAdmin,)
    readonly_fields = ("created", "modified")
    list_display = ("id", "name", "sentence_count", "audio", "image")
    list_filter = ("created", "modified")
    fieldsets = (
        (None, {"fields": ("name", "description")}),
        (_("Additional"), {"fields": ("audio", "image")}),
        (_("Read only"), {"fields": ("created", "modified")}),
    )

    @staticmethod
    def sentence_count(obj):
        return obj.sentences.count()
