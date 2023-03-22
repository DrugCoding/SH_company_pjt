from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# 회원가입 폼
class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

# # 수정 폼
# class ChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model
#         fields = ('name')