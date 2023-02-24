from django.contrib import admin
from .models import Doll, DollType


@admin.register(Doll)
class DollAdmin(admin.ModelAdmin):
    list_display = ('name', 'dolltype', 'price', 'image', 'on_sale')
    list_filter = ('dolltype',)


@admin.register(DollType)
class DollTypeAdmin(admin.ModelAdmin):

    list_display = ('name',)
