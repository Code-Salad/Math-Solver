# forms.py
from django import forms
from .models import *
# from Solver.views import *
  
class SumForm(forms.ModelForm):
  
    class Meta:
        model = Sum
        fields = ['topic', 'sum_img']