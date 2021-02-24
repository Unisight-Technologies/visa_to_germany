from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class Homepage(TemplateView):
    template_name= "index.html"

class Aboutpage(TemplateView):
    template_name= "aboutus.html"

class Contactpage(TemplateView):
    template_name= "contactus.html"

class Studentpage(TemplateView):
    template_name= "student_visa.html"

class Workingpage(TemplateView):
    template_name= "working_visa.html"

class Touristpage(TemplateView):
    template_name= "tourist_visa.html"

class Languagepage(TemplateView):
    template_name= "language_visa.html"
