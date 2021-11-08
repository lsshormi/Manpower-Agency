from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
   path("", views.home, name='home'),
   path("jobs", views.jobs, name='jobs'),
   path("about", views.about, name='about'),
   path("contact", views.contact, name='contact'),
   path("login", views.loginUser, name='login'),
   path("logout", views.logoutUser, name='logout'),
   path("signup", views.signupUser, name='signup'), 
   path("apply", views.apply, name='apply'),
   path("hire", views.hire, name='hire'),
]
