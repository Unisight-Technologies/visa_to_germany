from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . import scrap_news
from . import mailHandler
from . import models
from .models import News
import requests
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

#RECAPTCHA
import json
import urllib
from django.conf import settings
import environ

env = environ.Env()
#reading env files
environ.Env.read_env()

# Create your views here.
class Homepage(TemplateView):
    template_name= "index.html"

class Aboutpage(TemplateView):
    template_name= "aboutus.html"

class Contactpage(TemplateView):
    template_name= "contactus.html"
    def post(self, request):

        form = request.POST
        name = form.get('name')
        email = form.get('email')
        phone = form.get('phone')
        subject = form.get('subject')
        message = form.get('message')

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if result['success']:
            new_contact = models.Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
            )
            new_contact.save()
            mailHandler.sendMailToUser(request.POST.get('name'), request.POST.get('email'))
            mailHandler.sendMailToVisaToCanada(request.POST.get('name'), request.POST.get('email'),request.POST.get('phone'),request.POST.get('subject'),request.POST.get('message'))
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            context={
            'SITE_KEY': env('RECAPTCHA_SITE_KEY')
            }
            return render(request,"contactus.html",context = context)

class Studentpage(TemplateView):
    template_name= "student_visa.html"

class Workingpage(TemplateView):
    template_name= "working_visa.html"

class Touristpage(TemplateView):
    template_name= "tourist_visa.html"

class Languagepage(TemplateView):
    template_name= "language_visa.html"

class Feespage(TemplateView):
    template_name= "visa_fees.html"

class Familypage(TemplateView):
    template_name= "family_reunion.html"
class policy(TemplateView):
    template_name= "policy.html"

class terms(TemplateView):
    template_name= "terms.html"

class general(TemplateView):
    template_name= "generaldisclaimer.html"

class givesit(TemplateView):
    template_name= "givesit.html"

class Newspage(View):
    def get(self, request, *args, **kwargs):

        render_news = models.News.objects.all()
        context = {
            'news': render_news
        }

        return render(request, 'blogs_news.html', context=context)

@login_required(login_url='/admin/')
def refresh(request):
    # if(models.News.objects.all().exists()):
    #     for i in range(0, 5):
    #         old_news = models.News.objects.all()[0]
    #         old_news.delete()

    scrapper = scrap_news.Scrapper()

    for i in range(0,5):
        news = models.News.objects.create(
        	title=scrapper.titles[i],
        	date=scrapper.dates[i],
        	description=scrapper.descriptions[i],
        	url=scrapper.urls[i]
            )
        news.save()
        print(scrapper.urls[i])



        new_news = models.News.objects.get(title=scrapper.titles[i])


    return HttpResponse('News fetched successfully!')
