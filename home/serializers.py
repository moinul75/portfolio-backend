from rest_framework import serializers
from .models import AboutMe, WorkExperience, OtherProject, LatestProject, Skill, Testimonial, Education, Language, Info, Intro

class IntroSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Intro 
        fields = '__all__' 
        
class InfoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Info 
        fields = '__all__'


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class OtherProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherProject
        fields = '__all__'

class LatestProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestProject
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'