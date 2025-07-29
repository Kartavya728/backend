# api/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import About, Project, Skill, Event, PersonalInfo
from .serializers import (
    AboutSerializer,
    ProjectSerializer,
    SkillSerializer,
    EventSerializer,
    PersonalInfoSerializer
)

# ViewSets for list-based models
class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# A custom APIView for the singleton PersonalInfo model
class PersonalInfoView(APIView):
    def get(self, request, format=None):
        """
        Return the single PersonalInfo object.
        """
        # .first() returns the object or None if it doesn't exist
        info = PersonalInfo.objects.first()
        serializer = PersonalInfoSerializer(info, context={'request': request})
        return Response(serializer.data)