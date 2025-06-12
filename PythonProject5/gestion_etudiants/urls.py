"""
URL configuration for gestion_etudiants project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecole.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    # Groupes
    path('groupes/', views.liste_groupes, name='liste_groupes'),
    path('groupes/ajouter/', views.ajouter_groupe, name='ajouter_groupe'),
    path('groupes/modifier/<int:pk>/', views.modifier_groupe, name='modifier_groupe'),
    path('groupes/supprimer/<int:pk>/', views.supprimer_groupe, name='supprimer_groupe'),
    # Étudiants
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('etudiants/ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('etudiants/modifier/<int:pk>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('etudiants/supprimer/<int:pk>/', views.supprimer_etudiant, name='supprimer_etudiant'),
    # Enseignants
    path('enseignants/', views.liste_enseignants, name='liste_enseignants'),
    path('enseignants/ajouter/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('enseignants/modifier/<int:pk>/', views.modifier_enseignant, name='modifier_enseignant'),
    path('enseignants/supprimer/<int:pk>/', views.supprimer_enseignant, name='supprimer_enseignant'),
    # Cours
    path('cours/', views.liste_cours, name='liste_cours'),
    path('cours/ajouter/', views.ajouter_cours, name='ajouter_cours'),
    path('cours/modifier/<int:pk>/', views.modifier_cours, name='modifier_cours'),
    path('cours/supprimer/<int:pk>/', views.supprimer_cours, name='supprimer_cours'),
    # Absences
    path('absences/', views.liste_absences, name='liste_absences'),
    path('absences/ajouter/', views.ajouter_absence, name='ajouter_absence'),
    path('absences/modifier/<int:pk>/', views.modifier_absence, name='modifier_absence'),
    path('absences/supprimer/<int:pk>/', views.supprimer_absence, name='supprimer_absence'),
    # Import CSV
    path('absences/import/', views.import_absences, name='import_absences'),
    # Fiches
    path('absences/fiche_co_
