from django import forms
from .models import Performance

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = [
            'title',
            'customer',
            'start',
            'finish',
        ]
        # labels = {
        #     'title': '공사명',
        #     'customer': '발주처',
        #     'start': '공사시작',
        #     'finish': '공사종료',
        # }