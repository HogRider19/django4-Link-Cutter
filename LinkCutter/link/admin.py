from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'truncated_url', 'user']


admin.site.register(Link, LinkAdmin)