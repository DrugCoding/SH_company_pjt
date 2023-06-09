from django import forms
from .models import Construction

class ConstructionForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = (
            'title',
            'content',
            'image',
            'c_list',
            'ing_finish',
        )
        labels = {
            'title': '공사명',
            'content': '내용',
            'image': '사진',
            'c_list': '시공종목',
            'ing_finish': '공사진행현황',
        }