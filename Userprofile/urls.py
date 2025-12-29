from .views import home, projects, skills, contact
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'),  
    path('contact/', contact, name='contact'),
]