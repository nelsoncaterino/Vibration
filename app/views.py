from django.shortcuts import render # type: ignore 
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .models import Evenement, Card, emissions, Show

def player(request):
    return render(request, "modules/player.html")

def home(request):
    return render(request, "pages/home.html")

def carousel(request):
    return render(request, "module/carousel.html")

def navbar(request):
    return render(request, 'modules/navbar.html', {'request': request})

def podcast(request):
    return render(request, "pages/podcast.html")


def charts(request):
    return render(request, "pages/charts.html")

def teams(request):
    return render(request, "pages/teams.html")

def news(request):
    return render(request, "pages/news.html")

def newevents(request):
    return render(request, "pages/newevents.html")

def contact(request):
    return render(request, "pages/contact.html")

def livestream(request):
    return render(request, 'pages/livestream.html')

def emissions(request):
    return render(request, 'pages/grille_antenne.html')

def custom_404(request, exception):
    return render(request, "error/404.html")


def Stats_view(request):
    Stats = Stats.objects.all()
    return render(request, 'modules/stats.html', {'Stats': Stats})



def emission(request):
    days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    schedule = {day: Show.objects.filter(day_of_week=day).order_by('start_time') for day in days}
    return render(request, 'emissions.html', {'schedule': schedule})

