from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content']

# ClearableFileInput으로 여러 장의 image를 입력 받을 수 있음
# class ImageForm(ModelForm):
#     class Meta:
#         model = Photo
#         fields = ['image']
#         widgets = {
#             'image': ClearableFileInput(attrs={'multiple': True})
#         }