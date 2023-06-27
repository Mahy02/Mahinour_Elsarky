from django.contrib import admin

# Register your models here.
from .models import Home, About, Profile, Project, Internships, Achievement, StudentActivity, Category, Skills, Technology

# Home
admin.site.register(Home)


# About
class ProfileInLine(admin.TabularInline):
    model= Profile
    extra=1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines =[
        ProfileInLine,
    ]


# Skills
class SkillsInLine(admin.TabularInline):
    model= Skills
    extra=2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines=[
        SkillsInLine,
    ]

# Achievement
admin.site.register(Achievement)

# StudentActivity
admin.site.register(StudentActivity)

# Technology

admin.site.register(Technology)

# Internships

class TechnologyInline(admin.TabularInline):
    model = Internships.tools_and_technologies.through
    extra = 1

@admin.register(Internships)
class InternshipsAdmin(admin.ModelAdmin):
    inlines = [TechnologyInline]
    filter_horizontal = ('tools_and_technologies',)  # Display a horizontal filter widget for technologies

# Project
class TechnologyInline(admin.TabularInline):
    model = Project.tools_and_technologies.through
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechnologyInline]
    filter_horizontal = ('tools_and_technologies',)  # Display a horizontal filter widget for tools and technologies
    
