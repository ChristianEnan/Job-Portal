from django import forms
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
        }