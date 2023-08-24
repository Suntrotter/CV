from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import models
from .forms import Update_about_me, Image_display, Update_skills, Update_education, Update_projects


#class CreateProfileView(CreateView):
    #template_name = 'resume.html'
    #model = models.CV
    #fields = "__all__"
    #success_url = "/profiles"


#class ProfileViews(ListView):
    #template_name = 'profiles.html'
    #model = models.CV
    #context_object_name = "profiles"


def home(request):
    return render(request,"home.html")

def update_buttons(request):
    return render(request, "update_buttons.html")

def update_photo(request):
    if request.method == 'POST':
        form = Image_display(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/resume/')
    else:
        form = Image_display()
    return render(request, 'image.html', {'form': form})


def success(request):
    return render(request, "resume.html")

def resume(request):
    queryset = models.Image.objects.get()
    queryset_2 = models.About_me.objects.all()
    context = {
        'photo': queryset,
        'text': queryset_2
    }
    return render(request, "resume.html", context)

def update_aboutme(request):
    if request.method == "POST":
        form = Update_about_me(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('http://127.0.0.1:8000/resume/')
        else:
            return HttpResponse('Form not valid')
    else:
        form = Update_about_me()

    return render(request, "update_aboutme.html", {"form": form})

def update_skills(request):
    if request.method == "POST":
        form = Update_skills(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('http://127.0.0.1:8000/resume/')
        else:
            return HttpResponse('Form not valid')
    else:
        form = Update_skills()

    return render(request, "update_skills.html", {"form": form})


def update_education(request):
    if request.method == "POST":
        form = Update_education(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('http://127.0.0.1:8000/resume/')
        else:
            return HttpResponse('Form not valid')
    else:
        form = Update_education()

    return render(request, "update_education.html", {"form": form})


def update_projects(request):
    if request.method == "POST":
        form = Update_projects(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('http://127.0.0.1:8000/resume/')
        else:
            return HttpResponse('Form not valid')
    else:
        form = Update_projects()

    return render(request, "update_projects.html", {"form": form})


