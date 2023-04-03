from django import forms
from .models import Expenses

class ExpensesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Expenses
        fields = ['name', 'amount']
        

  