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
    