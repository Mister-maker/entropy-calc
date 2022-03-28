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
        exclude = ('output', 'url')

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EntropyCalcForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['csv_file'].required = True