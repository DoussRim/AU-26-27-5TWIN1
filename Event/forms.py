from django import forms
from .models import Event
class Date(forms.DateInput):
    input_type='date'
class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"
        # fields=('title','category','state')
        widgets={'evt_date':Date}
    