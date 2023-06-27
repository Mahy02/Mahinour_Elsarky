from django.shortcuts import render
from .models import Home, About, Profile, Project, Internships, Achievement, StudentActivity, Category, Skills, Technology


# Create your views here.
def index(request):

    #Home
    home= Home.objects.latest('updated')

    #About
    about = About.objects.latest('updated')
    profiles= Profile.objects.filter(about=about)

    #Skills
    categories= Category.objects.all()


# Internships
    internships = Internships.objects.all()

    # Student Activities
    student_activities = StudentActivity.objects.all()

    # Achievements
    achievements = Achievement.objects.all()

    #projects
    projects = Project.objects.order_by('-year').all()


    context ={
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'internships': internships,
        'student_activities': student_activities,
        'achievements': achievements,
        'projects': projects,
    }

    return render(request, 'index.html', context)
