from django.contrib import admin
from .models import Category, ExpenseRecord


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(ExpenseRecord)
class ExpenseRecordAdmin(admin.ModelAdmin):
    list_display = ('category', 'date', 'amount')
    list_filter = ['date', 'category']
    search_fields = ['date', 'category']
