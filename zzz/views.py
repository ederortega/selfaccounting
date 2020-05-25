from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .forms import ExpenseRecordForm
from .models import ExpenseRecord


class HomeView(TemplateView):
    template_name = 'zzz/home.html'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class UpdateEstateMixin():
    update = False

    def get_context_data(self, **kwargs):
        kwargs['update'] = self.update
        return super(UpdateEstateMixin, self).get_context_data(**kwargs)


class ExpenseRecordCreateView(UpdateEstateMixin, SuccessMessageMixin, CreateView):
    template_name = 'zzz/expense_add_edit.html'
    form_class = ExpenseRecordForm
    success_url = reverse_lazy('zzz:add')
    success_message = 'Expense record was created succesfully'


class ExpenseRecordUpdateView(UpdateEstateMixin, SuccessMessageMixin, UpdateView):
    template_name = 'zzz/expense_add_edit.html'
    form_class = ExpenseRecordForm
    model = ExpenseRecord
    success_message = 'Expense record was updated succesfully'
    update = True

    def form_valid(self, form):
        self.success_url = reverse_lazy(
            'zzz:edit',
            kwargs={'pk': self.object.pk}
        )
        return super(ExpenseRecordUpdateView, self).form_valid(form)
