from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CandidateProfile


class CandidateProfileForm(forms.ModelForm):

    class Meta:
        model = CandidateProfile

        fields = [
            'phone',
            'city',
            'skills',
            'experience',
            'github',
            'linkedin',
            'portfolio',
            'resume',
            'profile_image'
        ]

        widgets = {

            'phone': forms.TextInput(attrs={'class': 'form-control'}),

            'city': forms.TextInput(attrs={'class': 'form-control'}),

            'skills': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'experience': forms.TextInput(attrs={'class': 'form-control'}),

            'github': forms.URLInput(attrs={'class': 'form-control'}),

            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),

            'portfolio': forms.URLInput(attrs={'class': 'form-control'}),

            "profile_image": forms.FileInput(attrs={"class": "form-control","id": "id_profile_image"}),
        }

class RegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            "username",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

           field.widget.attrs.update({
                "class": "form-control",
                "placeholder": field.label,
                "autocomplete": "off",
          })