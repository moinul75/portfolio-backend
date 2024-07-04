from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InfoViewSet, 
    IntroViewSet,
    AboutMeViewSet, 
    WorkExperienceViewSet, 
    OtherProjectViewSet, 
    LatestProjectViewSet, 
    SkillViewSet, 
    TestimonialViewSet, 
    EducationViewSet, 
    LanguageViewSet)

router = DefaultRouter()
router.register(r'intro', IntroViewSet)
router.register(r'info', InfoViewSet)
router.register(r'about-me', AboutMeViewSet)
router.register(r'work-experience', WorkExperienceViewSet)
router.register(r'other-projects', OtherProjectViewSet)
router.register(r'latest-projects', LatestProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'education', EducationViewSet)
router.register(r'languages', LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]