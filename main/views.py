from django.shortcuts import render
from .forms import MessageForm
from .models import Portfolio, AboutMe, Project

def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
    
    form = MessageForm()
    portfolio = Portfolio.objects.last()
    about_me = AboutMe.objects.last()
    projects = Project.objects.all()
    context={
        "form": form,
        "about_me": about_me,
        "me": portfolio,
        "projects": projects
    }
    return render(request, "main/index.html", context)
