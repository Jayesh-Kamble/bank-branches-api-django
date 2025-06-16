from django.contrib import admin
from .models import Bank, Branch

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'created_at']
    search_fields = ['name', 'code']
    list_filter = ['created_at']

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch', 'bank', 'ifsc', 'city', 'state']
    search_fields = ['branch', 'ifsc', 'city']
    list_filter = ['bank', 'state', 'city']
    raw_id_fields = ['bank']
