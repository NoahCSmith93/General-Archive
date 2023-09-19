# Basic imports
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
# Class-based views imports
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# User auth imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Model imports
from .models import Project, Comment
from django.contrib.auth.models import User
# Forms imports
from .forms import CustomUserCreationForm, CommentForm
# Image handling imports
import uuid
import boto3
import os

#### Custom views

## Root
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

## Users
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "users/profile.html", {
        "user": user,
    })

def user_redirect(request):
    user_id = request.user.id
    return redirect('user_profile', user_id=user_id)


## Projects
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "projects/detail.html", {
        "project": project,

    })

@login_required
def add_project_photo(request, project_id):
    # input field must be named 'photo-file'
    photo_file = request.FILES.get('photo-file', None)
    AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    if photo_file:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        # uuid automatically generates unique filenames
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # update project's thumbnail to new url
            project = Project.objects.get(id=project_id)
            project.thumbnail = url
        except Exception as e:
            print('An error occured uploading to S3')
            print(e)
        # do something else if we didn't
    return redirect('project_detail', project_id=project_id)


## Comments


## Auth
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = CustomUserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
        }
    return render(request, 'registration/signup.html', context)


#### Class-based views




## Projects
class ProjectCreate(CreateView, LoginRequiredMixin):
    model = Project
    fields = ["title", "repository", "deployment", "thumbnail", "description"]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProjectUpdate(UpdateView, LoginRequiredMixin):
    model = Project
    fields = ["repository", "deployment", "thumbnail", "description"]

    def dispatch(self, request, *args, **kwargs):
        # Get the project to be operated on
        project = get_object_or_404(self.model, id=kwargs['pk'])
        # Check if the logged-in user is the owner of the project
        if request.user != project.user:
            return HttpResponseForbidden("You don't have permission to access this resource.")
        # Return to normal operation
        return super().dispatch(request, *args, **kwargs)

class ProjectDelete(DeleteView, LoginRequiredMixin):
    model = Project
    success_url = reverse_lazy("user_profile")
    
    def dispatch(self, request, *args, **kwargs):
        # Get the project to be operated on
        project = get_object_or_404(self.model, id=kwargs['pk'])
        # Check if the logged-in user is the owner of the project
        if request.user != project.user:
            return HttpResponseForbidden("You don't have permission to access this resource.")
        # Return to normal operation
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        user_id = self.request.user.id
        success_url = reverse("user_profile", kwargs={"user_id": user_id})
        return success_url
    

## Comments
class CommentCreate(CreateView, LoginRequiredMixin):
    model = Comment
    fields = ['content']

    def form_valid(self,form):
        form.instance.project = Project.objects.get(pk=self.kwargs['project_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_detail', args=[self.object.project.id])  # Redirect to the project detail after adding a comment    

class CommentUpdate(UpdateView, LoginRequiredMixin):
    model = Comment
    fields = ['content']

    def dispatch(self, request, *args, **kwargs):
        # Get the comment to be operated on
        comment = get_object_or_404(self.model, id=kwargs['pk'])
        # Check if the logged-in user is the owner of the comment
        if request.user != comment.user:
            return HttpResponseForbidden("You don't have permission to access this resource.")
        # Return to normal operation
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_detail', args=[self.object.project.id])  # Redirect to the project detail after updating the comment

class CommentDelete(DeleteView, LoginRequiredMixin):
    model = Comment

    def dispatch(self, request, *args, **kwargs):
        # Get the comment to be operated on
        comment = get_object_or_404(self.model, id=kwargs['pk'])
        # Check if the logged-in user is the owner of the comment
        if request.user != comment.user:
            return HttpResponseForbidden("You don't have permission to access this resource.")
        # Return to normal operation
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_detail', args=[self.object.project.id])  # Redirect to the project detail after deleting a comment


## Users
class ProfileUpdate(UpdateView, LoginRequiredMixin):
    model = User
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("user_profile")
    
    def get_success_url(self):
        user_id = self.request.user.id
        success_url = reverse("user_profile", kwargs={"user_id": user_id})
        return success_url
    