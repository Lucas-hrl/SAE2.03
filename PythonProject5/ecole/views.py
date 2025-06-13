from .models import Groupe, Etudiants, Enseignants, Cours, Absences
from .forms import GroupeForm, EtudiantForm, EnseignantForm, CoursForm, AbsenceForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models

# Groupes
def index (request):
    return render(request,"ecole/index.html")

