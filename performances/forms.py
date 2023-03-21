from django import forms
from .models import Performance

class PerformanceForm(forms.ModelForm):
    class Meta:
        Model = Performance
        fields = ['title', 'customer', 'start', 'finish']

