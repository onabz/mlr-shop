from django.contrib import admin
from .models import Doll, DollType
from django_summernote.admin import SummernoteModelAdmin


@admin.register(DollType)


@admin.register(Doll)
class DollAdmin(SummernoteModelAdmin):

    # list_display = ('name', 'category', 'price', 'image', 'on_sale')
    summernote_fields = ('description', 'safety_note', 'care_love_instructions')
