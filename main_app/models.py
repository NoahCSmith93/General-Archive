from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User

# Project model
# One to many with comments (project -|--< comments)
# One to many with users (project >--|- user)
class Project(models.Model):
    title = models.CharField(max_length=20)
    repository = models.CharField(max_length=200)
    deployment = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'project_id': self.id})



class Comment(models.Model):
    content = models.TextField(max_length=250)
    timestamp = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment with ID {self.id} made by User ID {self.user} on Project ID {self.project}"
    
    class Meta:
        ordering = ['-timestamp']