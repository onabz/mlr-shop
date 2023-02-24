from django.contrib import admin
from .models import Saying


@admin.register(Saying)
class SayingAdmin(admin.ModelAdmin):
    list_display = ('message', )
