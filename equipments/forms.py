from .models import Equipment
from django import forms

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['image', 'title', 'content']