from django import forms
from .models import Company, Job


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = [
            "name",
            "logo",
            "website",
            "email",
            "location",
            "description",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Company Name",
            }),

            "website": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "company@email.com",
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ahmedabad, India",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write company description...",
            }),

            "logo": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),

        }

class JobForm(forms.ModelForm):

    class Meta:

        model = Job

        fields = [
            "title",
            "company",
            "location",
            "salary",
            "description",
            "employment_type",
            "is_active",
        ]
    