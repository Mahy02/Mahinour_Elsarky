from django.contrib import admin

# Register your models here.
from .models import Home, About, Profile, Project, Internships, Achievement, StudentActivity, Category, Skills, Technology, Link

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

# Define an admin class for the Link model
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

# Register the Link model with its admin class
admin.site.register(Link, LinkAdmin)

# Define an inline admin class for the links field in Internships model
class InternshipsLinkInline(admin.TabularInline):
    model = Internships.links.through  # This is the intermediate model for the many-to-many relationship
    extra = 1  # Number of empty link forms to display

# Define an inline admin class for the links field in Project model
class ProjectLinkInline(admin.TabularInline):
    model = Project.links.through  # This is the intermediate model for the many-to-many relationship
    extra = 1  # Number of empty link forms to display



@admin.register(Internships)
class InternshipsAdmin(admin.ModelAdmin):
    inlines = [TechnologyInline, InternshipsLinkInline]
    filter_horizontal = ('tools_and_technologies',)  # Display a horizontal filter widget for technologies

# Project
class TechnologyInline(admin.TabularInline):
    model = Project.tools_and_technologies.through
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechnologyInline, ProjectLinkInline]
    filter_horizontal = ('tools_and_technologies',)  # Display a horizontal filter widget for tools and technologies
    
