from django.contrib import admin
from .models import Iqoption


class IqoptionAdmin(admin.ModelAdmin):
    model = Iqoption
    list_display = [
        'name',
    ]

    list_filter = [
    ]

    search_fields = [
        'name',
    ]

admin.site.register(Iqoption, IqoptionAdmin)

