from django.urls import path
from .views import HomeView, ExpenseRecordCreateView, ExpenseRecordUpdateView

app_name = 'zzz'
urlpatterns = [
    path('', HomeView.as_view(), name='dashboard'),
    path('add/', ExpenseRecordCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', ExpenseRecordUpdateView.as_view(), name='edit'),

]