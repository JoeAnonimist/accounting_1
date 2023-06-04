from django.contrib import admin
from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'normal']
    fields = ('name', 'number', 'normal')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'date', 'amount', 'account', 'direction')
    fields = ('transaction_id', 'date', 'amount', 'account', 'direction')


# Each class had to be in a separate line
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)