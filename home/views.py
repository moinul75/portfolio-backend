from rest_framework import viewsets
from .models import ( 
    Info, 
    Intro,
    AboutMe, 
    WorkExperience, 
    OtherProject, 
    LatestProject, 
    Skill, 
    Testimonial, 
    Education, 
    Language
)
from .serializers import (
    IntroSerializer, 
    InfoSerializer,
    AboutMeSerializer, 
    WorkExperienceSerializer, 
    OtherProjectSerializer, 
    LatestProjectSerializer, 
    SkillSerializer, 
    TestimonialSerializer, 
    EducationSerializer, 
    LanguageSerializer
) 

class IntroViewSet(viewsets.ModelViewSet): 
    queryset = Intro.objects.all()
    serializer_class = IntroSerializer 

class InfoViewSet(viewsets.ModelViewSet): 
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class OtherProjectViewSet(viewsets.ModelViewSet):
    queryset = OtherProject.objects.all()
    serializer_class = OtherProjectSerializer

class LatestProjectViewSet(viewsets.ModelViewSet):
    queryset = LatestProject.objects.all()
    serializer_class = LatestProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer