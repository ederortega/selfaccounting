from django.forms import ModelForm, DateInput, Select, NumberInput
from .models import Category, ExpenseRecord


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ExpenseRecordForm(ModelForm):
    class Meta:
        model = ExpenseRecord
        fields = ['category', 'date', 'amount']
        widgets = {
            'category': Select(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': NumberInput(attrs={'class': 'form-control'}),
        }
