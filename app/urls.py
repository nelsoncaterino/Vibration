    # myapp/urls.py
from django.conf import settings # type: ignore
from django.contrib import admin # type: ignore
from .views import player, home, podcast, charts, teams, news, contact, newevents, livestream, emissions, Stats_view, custom_404
from django.urls import path, include # type: ignore
from . import views
from django.urls import path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static


urlpatterns = [
    path('',home, name='home'),
    path('player', player, name='radio player'),
    path('podcast', podcast, name='podcast'),
    path('emissions', views.emissions, name='emissions'),
    path('teams', teams, name='teams'),
    path('news', news, name='news'),
    path('newevents', newevents, name='newevents'),
    path('contact', contact, name='contact'),
    path('livestream/', livestream, name='livestream'),
    path('stats/', views.Stats_view, name='stats'),

]

    
