# Basic imports
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
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
# Image handling imports
# import uuid
# import boto3
# import os

#### Custom views
def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "projects/detail.html", {
        "project": project,

    })


#### Class-based views

## Projects
class ProjectCreate(CreateView):
    model = Project
    fields = ["title", "repository", "deployment", "thumbnail", "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProjectUpdate(UpdateView):
    model = Project
    fields = ["repository", "deployment", "thumbnail", "description"]

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy("user_profile")
    def get_success_url(self):
        user_id = self.request.user.id
        success_url = reverse("user_profile", kwargs={"user_id": user_id})
        return success_url
    

## Comments

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy("project_detail")
    def get_success_url(self):
        return super().get_success_url()
    