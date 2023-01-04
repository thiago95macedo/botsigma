from django.contrib import admin
from .models import Iqoption


class IqoptionAdmin(admin.ModelAdmin):
    model = Iqoption
    list_display = [
        'name', 
        'cpf', 
        'mobile', 
        'trader_brokerage'
    ]

    list_filter = [
        'trader_brokerage'
    ]

    search_fields = [
        'name',
        'cpf'
    ]

admin.site.register(Iqoption, IqoptionAdmin)

