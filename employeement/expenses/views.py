from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Expenses
from .forms import ExpensesForm
from django_filters.views import FilterView
from .filters import ExpensesFilter


class ExpensesListView(FilterView):
    filterset_class = ExpensesFilter
    queryset = Expenses.objects.filter(is_deleted=False)
    template_name = 'expenses.html'
    paginate_by = 10


class ExpensesCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Expenses                                                                      # setting 'Stock' model as model
    form_class = ExpensesForm                                                             # setting 'StockForm' form as form
    template_name = "edit_expenses.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/expenses'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Expense has been created successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Expense'
        context["savebtn"] = 'Add to Expense'
        return context       

 
        
        
class ExpensesUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Expenses                                                                      # setting 'Stock' model as model
    form_class = ExpensesForm                                                              # setting 'StockForm' form as form
    template_name = "edit_expenses.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/expenses'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Expense has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Expense'
        context["savebtn"] = 'Update Expense'
        context["delbtn"] = 'Delete Expense'
        return context


