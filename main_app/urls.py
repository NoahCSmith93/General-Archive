from django.urls import path
from . import views

urlpatterns = [
    #### Root
    # Splash page and instructions
    path('', views.home, name='home'),
    # Technologies used, credits, details about blog
    # path('about/', views.about, name='about'),


    #### User:
    # The main profile page. This would display the user's name, email, bio, links, profile picture, and other personal details.
    # path('user/<int:id>/', views.user_profile, name='user_profile'),
    # To edit the profile details like name, bio, and links.
    # path('user/<int:id>/edit/', views.edit_profile, name='edit_profile'),
    # List all users projects
    # path('user/<int:id>/projects/', views.user_projects_list, name='user_projects_list'),
    # Add a new project for user


    #### Projects:
    # Shows the most recently created projects
    # path('projects/', views.projects_index, name='index'),
    # Projects info page will also include comments, stored in their own table.
    # Project info page including thumbnail. Links to owning user page, github repo, deployment page.
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    # Project create page
    path('projects/create/', views.ProjectCreate.as_view(), name='project_create'),
    # Project edit route
    path('projects/<int:id>/edit', views.ProjectUpdate.as_view(), name='project_edit'),
    # Project delete route
    path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name='project_delete'),
    

    # url for s3 upload (thumbnail)
    # path('projects/<int:project_id>/add_photo', views.add_photo, name='add_photo'),

    #### Comments:
    # path('projects/<int:project_id>/comments/new/', views.add_comment, name='add_comment'),
    # path('projects/<int:project_id>/comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    # path('projects/<int:project_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    #### Auth:
    # path('accounts/signup/', views.signup, name='signup'),
    
]