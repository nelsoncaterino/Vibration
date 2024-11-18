from django import pytest
from django.test import TestCase
from django.test import RequestFactory
from django.contrib import admin
from django.urls import reverse
from django.contrib.admin.sites import app
from app.models import Evenement, Visitor, PlayedTrack

@pytest.mark.django_db
def test_evenement_admin_registered():
    # Vérifier que le modèle Evenement est bien enregistré dans l'admin
    assert app.is_registered(Evenement), "Le modèle Evenement n'est pas enregistré dans l'administration"

@pytest.mark.django_db
def test_visitor_admin_registered():
    # Vérifier que le modèle Visitor est bien enregistré dans l'admin
    assert app.is_registered(Visitor), "Le modèle Visitor n'est pas enregistré dans l'administration"

@pytest.mark.django_db
def test_playedtrack_admin_registered():
    # Vérifier que le modèle PlayedTrack est bien enregistré dans l'admin
    assert app.is_registered(PlayedTrack), "Le modèle PlayedTrack n'est pas enregistré dans l'administration"

@pytest.mark.django_db
def test_evenement_list_display(admin_client):
    # Vérifier que les champs sont bien affichés dans l'interface d'administration
    url = reverse("admin:your_app_name_evenement_changelist")
    response = admin_client.get(url)
    assert response.status_code == 200
    for field in ['titre', 'date_debut', 'date_fin']:
        assert field in str(response.content), f"{field} n'est pas affiché dans la liste des événements"

@pytest.mark.django_db
def test_playedtrack_cover_preview(admin_client, playedtrack_factory):
    # Vérifier que la prévisualisation de la couverture fonctionne
    playedtrack = playedtrack_factory()
    url = reverse("admin:your_app_name_playedtrack_changelist")
    response = admin_client.get(url)
    assert response.status_code == 200
    assert "No cover" in str(response.content) or f'<img src="{playedtrack.cover.url}"' in str(response.content)
