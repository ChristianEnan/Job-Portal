from django import forms


class ProfileCompletionForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    profile_photo = forms.FileField(required=False, widget=forms.ClearableFileInput())
    phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={"placeholder": "Phone number"}))
    location = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={"placeholder": "Location"}))
    education = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "School, college, degree, year", "rows": 3}))
    key_skills = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Python, Django, SQL", "rows": 3}))
    languages = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "English, Hindi, Gujarati", "rows": 3}))
    internships = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Company, role, duration", "rows": 3}))
    projects = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Project name, stack, impact", "rows": 3}))
    profile_summary = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Short professional summary", "rows": 4}))
    accomplishments = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Awards, achievements, certifications", "rows": 3}))
    competitive_exams = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Exams, ranks, scores", "rows": 3}))
    employment = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Work experience or internships", "rows": 3}))
    academic_achievements = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Grades, distinctions, honors", "rows": 3}))
    resume = forms.FileField(required=False, widget=forms.ClearableFileInput())
    experience_years = forms.IntegerField(required=False, min_value=0, initial=0, widget=forms.NumberInput(attrs={"min": 0}))