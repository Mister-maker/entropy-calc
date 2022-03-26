# import form class from django
from django import forms
  
# import EntropyCalc from models.py
from .models import EntropyCalc
  
# create a ModelForm
class EntropyCalcForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EntropyCalc
        fields = "__all__"