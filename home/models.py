from django.db import models

# Create your models here.

class AboutMe(models.Model):  
    language = models.TextField(blank=True,null=True)
    framework = models.TextField(blank=True,null=True)
    chatbots = models.TextField(blank=True,null=True)
    tools  = models.TextField(blank=True,null=True)
    editor_journey = models.TextField(blank=True,null=True)
    operating_system = models.CharField(max_length=255,null=True,blank=True)
    experience = models.CharField(max_length=255,null=True,blank=True)
    current_employe = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.current_employe 
    
class WorkExperience(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()
    environment = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}" 
    

class OtherProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    technology_stack = models.TextField()
    more_info_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name 
    

class LatestProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() 
    image = models.FileField(upload_to='projects_img',null=True,blank=True)
    technology_stack = models.TextField()
    team_size = models.IntegerField()
    more_info_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name 
    
    
class Intro(models.Model): 
    full_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255) 
    profile_img = models.FileField(upload_to='profile_imge/',null=True,blank=True) 
    info_email = models.EmailField(unique=True,null=True,blank=True)
    fb_link = models.URLField(null=True,blank=True)
    linkedin_link = models.URLField(null=True,blank=True)
    github_link = models.URLField(null=True,blank=True)
    telegram_link = models.URLField(null=True,blank=True) 
    stackoverflow_link = models.URLField(null=True,blank=True)
    whatsapp_link = models.URLField(null=True,blank=True)
    
    
    def __str__(self) -> str:
        return self.full_name  
    
    
class Info(models.Model): 
    location = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    cv_link = models.CharField(null=True,blank=True,max_length=255)
    contact_num = models.CharField(max_length=20,null=True,blank=True) 
    
    
    def __str__(self) -> str:
        return f"{self.email } - {self.location}"
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.proficiency}"

class Testimonial(models.Model):
    content = models.TextField()
    author_name = models.CharField(max_length=255)
    author_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.author_name} - {self.author_title}"
    
class Education(models.Model):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} from {self.institution} ({self.start_year}-{self.end_year})"
    
class Language(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.proficiency}"
    
    
    
    
    
    