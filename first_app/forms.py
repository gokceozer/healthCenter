from django import forms
from first_project import settings
from first_app.models import Patient, Past_Location

class NewPatientForm(forms.ModelForm):
    class Meta():
        model = Patient
        fields = '__all__'


class PastLocationForm(forms.ModelForm):
    class Meta():
        model = Past_Location
        fields = '__all__'

LocationFormSet = forms.modelformset_factory(
    Past_Location,
    fields='__all__',
    extra=1,
    widgets={
        'location': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Location Name here'
            }
        )
    }
)
