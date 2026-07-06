from django import forms
from django.forms.widgets import TextInput, FileInput, PasswordInput

from account_module.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','avatar']
        widgets={
            'username':TextInput(attrs={
                'class':'form-control'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': FileInput(attrs={
                'class': 'form-control'
            })
        }


class EditPasswordForm(forms.Form):
    current_password=forms.CharField(label='رمز فعلی', widget=PasswordInput(attrs={
        'class':'form-control'
    }))
    new_password=forms.CharField(min_length=8,max_length=12,label='رمز جدید', widget=PasswordInput(attrs={
        'class':'form-control'
    }))
    confirm_new_password=forms.CharField(label='تکرار رمز جدید', widget=PasswordInput(attrs={
        'class':'form-control'
    }))