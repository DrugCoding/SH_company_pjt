from .models import Equipment, EquipImage
from django import forms
from django.forms import ClearableFileInput

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['image', 'title', 'content']
        labels = {'image' : '메인 이미지',
                  'title': '장비명',
                  'content': '장비 설명'
                  }
    
# 장비 디테일 페이지에 등록하는 이미지
class EquipImageForm(forms.ModelForm):
    class Meta:
        model = EquipImage
        fields = ['equip_img']
        widgets = {
            'equip_img': ClearableFileInput(attrs={'multiple': True})
        }
        labels = {
            'equip_img': '추가 이미지'
        }