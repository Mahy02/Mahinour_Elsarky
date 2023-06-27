from django.db import models

# Create your models here.
 


# HOME SECTION

class Home(models.Model):
    name= models.CharField(max_length=100)
    greetings_1 = models.CharField(max_length=10)
    greetings_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to = 'picture/')
    #save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.name
    


# ABOUT SECTION

class About(models.Model):
   heading = models.CharField(max_length=200)
   career= models.CharField(max_length=100)
   description= models.TextField(blank=False)
   profile_img= models.ImageField(upload_to='profile/')

   updated= models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.career
   
class Profile(models.Model):
   about = models.ForeignKey(About, on_delete=models.CASCADE)
   social_name= models.CharField(max_length=10)
   link = models.URLField(max_length=200)



# SKILLS SECTION

class Category(models.Model):
   name= models.CharField(max_length=20)
   
   updated= models.DateTimeField(auto_now=True)

   class Meta:
      verbose_name= 'Skill'
      verbose_name_plural= 'Skills'

   def __str__(self):
        return self.name
   
   
class Skills(models.Model):
   category= models.ForeignKey(Category, on_delete=models.CASCADE)
   skill_name= models.CharField(max_length=50)



# INTERNSHIPS SECTION
#company name, role, from, to, description, Technologies used, image1, image2

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Internships(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=False)
    tools_and_technologies = models.ManyToManyField(Technology)   #many internships can have many technologies and one technology can be in many internships
    image1 = models.ImageField(upload_to='internships/', null=True, blank=True)
    image2 = models.ImageField(upload_to='internships/', null=True, blank=True)

    def __str__(self):
        return self.company_name
    

# PROJECTS SECTION
#project name, year, projecttype, description, tools and technologies
    
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    project_type = models.CharField(max_length=500)
    description = models.TextField(blank=False)
    tools_and_technologies = models.ManyToManyField(Technology)

    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name



# STUDENT ACTIVITIES 
#name,role, from, to, description, image1, image2

class StudentActivity(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=False)
    image1 = models.ImageField(upload_to='student_activities/')
    image2 = models.ImageField(upload_to='student_activities/')

    def __str__(self):
        return self.name
    


# ACHIEVEMNTS
#name, year, description

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


    
