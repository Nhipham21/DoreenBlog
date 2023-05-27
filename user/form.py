from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Comment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(required=False, label='User Name')
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': None,
        }


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = Profile
        fields = ['image']


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False, label='Để lại bình luận')

    class Meta:
        model = Comment
        fields = ['body']
