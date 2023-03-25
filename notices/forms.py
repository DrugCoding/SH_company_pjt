from django import forms
from .models import Notice 

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content']

# class ImageForm(NoticeForm): #extending form
#     images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta(NoticeForm.Meta):
#         fields = NoticeForm.Meta.fields + ['images',]