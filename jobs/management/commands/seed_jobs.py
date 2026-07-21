from django.core.management.base import BaseCommand
from jobs.models import Company, Job


class Command(BaseCommand):
    help = "Insert demo companies and jobs"

    def handle(self, *args, **kwargs):

        companies = [
            "Google",
            "Microsoft",
            "Amazon",
            "Infosys",
            "TCS",
            "Wipro",
            "Accenture",
            "IBM",
            "Deloitte",
            "Capgemini",
        ]

        company_objects = {}

        for name in companies:
            company, created = Company.objects.get_or_create(
                name=name,
                defaults={
                    "location": "India",
                    "website": f"https://{name.lower().replace(' ', '')}.com",
                },
            )
            company_objects[name] = company

        jobs = [
            ("Python Developer", "Google", "Ahmedabad", "8 LPA"),
            ("Django Developer", "Google", "Remote", "10 LPA"),
            ("Frontend Developer", "Microsoft", "Bangalore", "9 LPA"),
            ("Backend Developer", "Amazon", "Hyderabad", "12 LPA"),
            ("Full Stack Developer", "Infosys", "Pune", "7 LPA"),
            ("AI Engineer", "IBM", "Ahmedabad", "11 LPA"),
            ("Machine Learning Engineer", "Google", "Remote", "15 LPA"),
            ("Software Engineer", "TCS", "Ahmedabad", "6 LPA"),
            ("Python Intern", "Capgemini", "Remote", "25000/month"),
            ("React Developer", "Accenture", "Mumbai", "8 LPA"),
            ("Java Developer", "Wipro", "Pune", "7 LPA"),
            ("DevOps Engineer", "Amazon", "Bangalore", "13 LPA"),
            ("Data Analyst", "Deloitte", "Ahmedabad", "9 LPA"),
            ("Cloud Engineer", "Microsoft", "Hyderabad", "12 LPA"),
            ("QA Engineer", "Infosys", "Ahmedabad", "6 LPA"),
            ("Flutter Developer", "IBM", "Remote", "8 LPA"),
            ("Node.js Developer", "Google", "Ahmedabad", "9 LPA"),
            ("UI/UX Designer", "Accenture", "Remote", "7 LPA"),
            ("Cyber Security Analyst", "TCS", "Delhi", "10 LPA"),
            ("Data Scientist", "Amazon", "Bangalore", "16 LPA"),
        ]

        for title, company, location, salary in jobs:
            Job.objects.get_or_create(
                title=title,
                company=company_objects[company],
                defaults={
                    "location": location,
                    "salary": salary,
                    "description": f"Hiring for {title}",
                    "employment_type": "full_time",
                    "is_active": True,
                },
            )

        self.stdout.write(self.style.SUCCESS("Demo Companies & Jobs Added Successfully"))