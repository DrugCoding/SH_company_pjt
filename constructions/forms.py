from django import forms
from .models import Constructions

class ConstructionForm(forms.ModelForm):
    class Meta:
        model = Constructions
        fields = (
            'title',
            'content',
            'image',
            'c_list',
        )
        labels = {
            'title': '공사명',
            'content': '내용',
            'image': '사진',
            'c_list': '시공종목',
        }