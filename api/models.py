# api/models.py
from django.db import models

# Section 1: About Info
class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        # This will make the admin panel say "Abouts" instead of "Abouts"
        verbose_name_plural = "About Entries"

    def __str__(self):
        return self.title

# Section 2: Projects
# api/models.py

# NEW MODEL for our tech stack options
class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    # This will make it look nice in the admin panel
    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name

# UPDATED Project model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    github_link = models.URLField(max_length=200, blank=True, null=True)
    
    # The new Many-to-Many field for tech stack
    technologies = models.ManyToManyField(Technology, related_name="projects")
    
    # The new boolean field
    is_deployed = models.BooleanField(default=False)
    
    # We already have this, and it will be used when is_deployed is True
    visit_link = models.URLField(max_length=200, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Section 3: Skill Set
class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='skill_images/')

    def __str__(self):
        return self.title

# Section 4: Events and Competitions
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    
    class Meta:
        verbose_name_plural = "Events and Competitions"

    def __str__(self):
        return self.title

# Section 5: Personal Links and Resume
class PersonalInfo(models.Model):
    github_link = models.URLField(max_length=200)
    linkedin_link = models.URLField(max_length=200)
    resume_pdf = models.FileField(upload_to='resumes/')
    
    class Meta:
        verbose_name_plural = "Personal Info"

    def __str__(self):
        # Since there will only be one, this name is fine
        return "My Personal Info"