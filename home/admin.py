from django.contrib import admin 
from .models import AboutMe,Info,Intro,Language,Skill,Education,Testimonial,WorkExperience,OtherProject,LatestProject

# Register your models here. 
admin.site.register(Intro)
admin.site.register(Info)
admin.site.register(AboutMe)
admin.site.register(Language)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Testimonial)
admin.site.register(WorkExperience)
admin.site.register(OtherProject)
admin.site.register(LatestProject) 



