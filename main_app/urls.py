from django.urls import path
from . import views
from .views import CommentCreate, CommentUpdate, CommentDelete

urlpatterns = [
    #### Root
    # Splash page and instructions
    path('', views.home, name='home'),
    # Technologies used, credits, details about blog
    path('about/', views.about, name='about'),


    #### User:
    # The main profile page. This would display the user's name, email, bio, links, profile picture, and other personal details.
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    # To edit the user info (name and email).
    path('user/<int:pk>/edit/', views.ProfileUpdate.as_view(), name='profile_edit'),
    # To edit the profile links.
    path('editlinks/<int:pk>/', views.ProfileLinksUpdate.as_view(), name='profile_links_edit'),
    # User redirect route - redirects to the proper user ID
    path('user/', views.user_redirect, name='user_redirect'),
    # url for s3 upload (profile photo)
    path('user/<int:user_id>/add_photo', views.add_profile_photo, name='add_profile_photo'),


    #### Projects:
    # Shows the most recently created projects
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    # Projects info page will also include comments, stored in their own table.
    # Project info page including thumbnail. Links to owning user page, github repo, deployment page.
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    # Project create page
    path('projects/create/', views.ProjectCreate.as_view(), name='project_create'),
    # Project edit route
    path('projects/<int:pk>/edit', views.ProjectUpdate.as_view(), name='project_edit'),
    # Project delete route
    path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name='project_delete'),
    
    # url for s3 upload (thumbnail)
    path('projects/<int:project_id>/add_photo', views.add_project_photo, name='add_project_photo'),

    #### Comments:
    path('projects/<int:project_id>/comments/new/', views.CommentCreate.as_view(), name='add_comment'),
    path('projects/<int:project_id>/comments/<int:pk>/edit/', views.CommentUpdate.as_view(), name='edit_comment'),
    path('projects/<int:project_id>/comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='delete_comment'),


    #### Auth:
    path('accounts/signup/', views.signup, name='signup'),
    
]