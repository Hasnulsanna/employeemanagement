from django.urls import path
#from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ExpensesListView.as_view(), name='expenses'),
    path('new-expenses', views.ExpensesCreateView.as_view(), name='edit-expenses'),
    path('expenses/<pk>/edit', views.ExpensesUpdateView.as_view(), name='edit-expenses'),
]