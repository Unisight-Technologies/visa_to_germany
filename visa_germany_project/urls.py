"""visa_germany_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from visa_germany_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage.as_view(),name="index"),
    path('aboutus/', views.Aboutpage.as_view(),name="aboutus"),
    path('contactus/', views.Contactpage.as_view(),name="contactus"),
    path('student_visa/', views.Studentpage.as_view(),name="student_visa"),
    path('working_visa/', views.Workingpage.as_view(),name="working_visa"),
    path('tourist_visa/', views.Touristpage.as_view(),name="tourist_visa"),
    path('language_visa/', views.Languagepage.as_view(),name="language_visa"),
    path('visa_fees/', views.Feespage.as_view(),name="visa_fees"),
    path('family_reunion/', views.Familypage.as_view(),name="family_reunion"),
    path('blogs_news/', views.Newspage.as_view(),name="blogs_news"),
    path('coming_soon/', views.Comingpage.as_view(),name="coming_soon"),
    path('spain_coming_soon/',views.Spain_Comingpage.as_view(),name="spain_coming_soon"),
    path('Denmark_coming_soon/',views.Denmark_Comingpage.as_view(),name="Denmark_coming_soon"),
    path('Italy_coming_soon/',views.Italy_Comingpage.as_view(),name="Italy_coming_soon"),
    path('Greece_coming_soon/',views.Greece_Comingpage.as_view(),name="Greece_comingsoon"),
    path('policy/',views.policy.as_view(),name="policy"),
    path('terms/',views.terms.as_view(),name="terms"),
    path('givesit/',views.givesit.as_view(),name="givesit"),
    path('generaldisclaimer/',views.general.as_view(),name="general"),

    path('refresh/', views.refresh, name='refresh'),

]
