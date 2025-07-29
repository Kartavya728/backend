# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AboutViewSet,
    ProjectViewSet,
    SkillViewSet,
    EventViewSet,
    PersonalInfoView
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'events', EventViewSet)

# The API URLs are now determined automatically by the router.
# We also add the custom URL for our PersonalInfo view.
urlpatterns = [
    path('', include(router.urls)),
    path('personal-info/', PersonalInfoView.as_view(), name='personal-info'),
]