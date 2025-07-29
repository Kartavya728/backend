# api/migrations/0002_seed_technologies.py
from django.db import migrations

# NO IMPORT FROM .models HERE!

TECHNOLOGIES = [
    "Python", "JavaScript", "TypeScript", "HTML5", "CSS3",
    "React", "Next.js", "Node.js", "Express", "Flask", "Django",
    "TensorFlow", "PyTorch", "OpenCV", "Scikit-learn",
    "MongoDB", "PostgreSQL", "MySQL", "SQLite", "SQL",
    "Flutter", "Dart",
    "Git", "GitHub", "Docker",
    "Tailwind CSS", "Framer Motion",
    "Blockchain", "Spline", "Gemini", "GPT", "N8N",
    "Arduino IDE", "DSA",
]

def add_technologies(apps, schema_editor):
    Technology = apps.get_model('api', 'Technology')
    for tech in TECHNOLOGIES:
        Technology.objects.create(name=tech)

def remove_technologies(apps, schema_editor):
    Technology = apps.get_model('api', 'Technology')
    Technology.objects.filter(name__in=TECHNOLOGIES).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_technologies, remove_technologies)
    ]