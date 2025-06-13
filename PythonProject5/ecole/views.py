from .models import Groupe, Etudiants, Enseignants, Cours, Absences
from .forms import GroupeForm, EtudiantForm, EnseignantForm, CoursForm, AbsenceForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models

# Page d'accueil
def index (request):
    return render(request,"ecole/index.html")

#Groupes
def ajouter_groupe(request):
    form = GroupeForm()
    return render(request, "ecole/ajouter_groupe.html", {"form": form})

def traitement_groupe(request):
    form = GroupeForm(request.POST)
    if form.is_valid():
        Groupe = form.save()
        return HttpResponseRedirect("/ecole/liste_groupes")
    else:
        return render(request,"ecole/ajouter_groupe.html/", {"form":form})

def liste_groupes(request):
    liste_groupe = list(models.Groupe.objects.all())
    return render(request, "ecole/liste_groupes.html", {"liste_g":liste_groupe})

def afficher_groupe(request,id):
    groupe= models.Groupe.objects.get(pk=id)
    return render (request, "ecole/afficher_groupe.html", {"groupe": groupe})

def update_groupe(request,id):
    groupe = models.Groupe.objects.get(pk=id)
    dico= groupe.dico()
    form = GroupeForm(dico)
    return render(request,"ecole/ajouter_groupe.html", {"form":form, "id":id})

def traitement_update_groupe (request,id):
    gform = GroupeForm(request.POST)
    if gform.is_valid():
        Groupe = gform.save(commit = False)
        Groupe.id = id
        Groupe.save()
        return HttpResponseRedirect("/ecole/liste_groupes")
    else:
        return render(request, "ecole/ajouter_groupe.html", {"gform": gform , "id":id})

def supprimer_groupe(request,id):
    groupe = models.Groupe.objects.get(pk=id)
    groupe.delete()
    return HttpResponseRedirect("/ecole/liste_groupes")


