from django.contrib import admin
from .models import Doll, DollType
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Doll)
class DollAdmin(SummernoteModelAdmin):

    list_display = ('name', 'dolltype', 'price', 'image', 'on_sale')
    list_filter = ('dolltype',)
    summernote_fields = (
        'description', 'safety_note', 'care_love_instructions'
    )


@admin.register(DollType)
class DollTypeAdmin(admin.ModelAdmin):

    list_display = ('name',)
