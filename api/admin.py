# api/admin.py
from django.contrib import admin
from .models import About, Project, Skill, Event, PersonalInfo ,Technology # Import Technology

admin.site.register(Technology)

# Update the Project admin view
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_deployed', 'created_at')
    list_filter = ('is_deployed', 'technologies')
    
    # This makes the many-to-many selection much nicer
    filter_horizontal = ('technologies',)

# Unregister the old simple admin if it's there and register the new one
# (This is good practice but might not be necessary if you started fresh)
if admin.site.is_registered(Project):
    admin.site.unregister(Project)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title',)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Special admin configuration for the singleton PersonalInfo model
class PersonalInfoAdmin(admin.ModelAdmin):
    # This prevents users from adding more than one PersonalInfo instance
    def has_add_permission(self, request):
        return not PersonalInfo.objects.exists()

# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)