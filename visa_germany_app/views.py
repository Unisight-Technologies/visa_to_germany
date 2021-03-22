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

        new_contact = models.Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message

        )
        new_contact.save()
        mailHandler.sendMailToUser(name, email)
        mailHandler.sendMailToVisaToCanada(name, email, phone, subject, message)
        messages.success(request, "Your query has been successfully submitted. We will get back to you soon.")
        return redirect("contactus")

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
class Comingpage(TemplateView):
    template_name= "coming_soon.html"

class Spain_Comingpage(TemplateView):
    template_name= "spain_coming_soon.html"

class Denmark_Comingpage(TemplateView):
    template_name= "Denmark_coming_soon.html"

class Italy_Comingpage(TemplateView):
    template_name= "Italy_coming_soon.html"

class Greece_Comingpage(TemplateView):
    template_name= "Greece_coming_soon.html"

class policy(TemplateView):
    template_name= "policy.html"

class terms(TemplateView):
    template_name= "terms.html"

class general(TemplateView):
    template_name= "generaldisclaimer.html"


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
