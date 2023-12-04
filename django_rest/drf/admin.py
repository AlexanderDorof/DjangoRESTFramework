from django.contrib import admin
from .models import Wonder


class WonderCustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created', 'place', 'current_status')


admin.site.register(Wonder, WonderCustomAdmin)
