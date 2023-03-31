from .models import Equipment
from django import forms

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['image', 'title', 'content']
        labels = {'image' : '이미지',
                  'title': '장비명',
                  'content': '장비 설명'
                  }