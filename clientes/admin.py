from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
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

admin.site.register(Cliente, ClienteAdmin)

