# GA-General Archive - By Team Granular Archivists 📖
Our blog is a platform designed for GA students to showcase, manage, and share their projects. With user authentication, integrated comments, and personal profiles, each student can provide details about their project, get feedback, and display links to deployment and their GitHub repositories..

# Link 
https://general-archive.onrender.com/

# Technologies Used
- Django
- Python
- Javascript
- AWS
- SQL
- CSS
- Materialize
- HTML


# User Stories
- As a GA student, I want to sign up for an account, because I need a personal space to upload and showcase my projects.
- As a GA student, I want to log in to the blog, because I want to manage and update my projects and view comments.
- AAU, I want to be able to navigate to separate pages for About and All Projects using a navbar because I enjoy easy accessibility. 
- AAU, when I visit the About page, I want to view some details about the project application and set a description because I want to introduce myself and give context about my work and journey.
- AAU, when I click the Profile page, I want to see a page listing of all of my projects and personal information because I want to see how many projects I have submitted and update my personal profile.
- AAU, when I visit the All Projects page, I want to view a list of all projects from the database (index view) that displays each of the attributes of a project.
- AAU, when I click on a project card on the index page, I want to be taken to a details page where I can see all attributes of the project.
- AAU, when viewing a projects detail page, I want to click EDIT to update that projects attributes (like deployment link, Github repo, description, thumbnail image), because I may need to update or correct some information.
- AAU, when viewing a projects detail page, I want to click DELETE to remove that project from the database because I may decide some projects are no longer relevant or I want to declutter my portfolio.
- AAU, when I visit the detail page for a project, I want to see a list of comments for that project because I want to see feedback and engagement from viewers.
- AAU, when I visit the detail page for a project, I want to be able to add a comment for a project because I want to interact.
- AAU, I want to add a profile picture to my projects page, because I want to personalize my profile.
- AAU, I want my personal details and projects to be secure, because I want to protect my privacy and intellectual property.

# URLs

### /home
Splash page and instructions

### /about
Technologies used and credits

### /user/<int:id>
User's profile page. Name, email, bio, links, etc.

### /projects
Projects index page. Shows the most recently created projects.

### /projects/<int:id>
Project info page including thumbnail. Links to owning user page, github repo, deployment page.
Projects info page will also include comments, stored in their own table.

# Wireframes
<img src="https://i.imgur.com/dDBiGpK.png">
<img src="https://i.imgur.com/ZKTLimW.png">
<img src="https://i.imgur.com/FhSfL7H.png">
<img src="https://i.imgur.com/tl0QPK9.png">
<img src="https://i.imgur.com/GSucYdR.png">

# ERD
![Alt text](https://i.imgur.com/lTHRJE6.png)

# Screenshots
![image](https://github.com/JordonM/General-Archive/assets/14878928/d1681291-42ce-4e1e-827f-fcefff2e266b)

# Next Steps
Add more CSS to individual pages

