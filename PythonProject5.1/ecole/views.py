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
    groupe= models.Groupe.objects.get(id_gr=id)
    return render (request, "ecole/afficher_groupe.html", {"groupe": groupe})

def update_groupe(request,id):
    groupe = models.Groupe.objects.get(id_gr=id)
    dico= groupe.dico()
    form = GroupeForm(dico)
    return render(request,"ecole/ajouter_groupe.html", {"form":form, "id":id})

def traitement_update_groupe(request, id):
    groupe_existant = models.Groupe.objects.get(id_gr=id)
    gform = GroupeForm(request.POST, instance=groupe_existant)  # Utilisation de instance
    if gform.is_valid():
        groupe = gform.save()
        return HttpResponseRedirect("/ecole/liste_groupes")
    else:
        return render(request, "ecole/ajouter_groupe.html", {"gform": gform, "id": id})

def supprimer_groupe(request,id):
    groupe = models.Groupe.objects.get(id_gr=id)
    groupe.delete()
    return HttpResponseRedirect("/ecole/liste_groupes")


#Etudiants
def ajouter_etudiant(request):
    form = EtudiantForm()
    return render(request, "ecole/ajouter_etudiant.html", {"form": form})

def traitement_etudiant(request):
    form = EtudiantForm(request.POST)
    if form.is_valid():
        Etudiants = form.save()
        return HttpResponseRedirect("/ecole/liste_etudiants")
    else:
        return render(request,"ecole/ajouter_etudiant.html/", {"form":form})

def liste_etudiants(request):
    liste_etudiants = list(models.Etudiants.objects.all())
    return render(request, "ecole/liste_etudiants.html", {"liste_e":liste_etudiants})

def afficher_etudiant(request,id):
    etudiant= models.Etudiants.objects.get(id_etu=id)
    return render (request, "ecole/afficher_etudiant.html", {"etudiant": etudiant})

def update_etudiant(request,id):
    etudiant = models.Etudiants.objects.get(id_etu=id)
    dico= etudiant.dico()
    form = EtudiantForm(dico)
    return render(request,"ecole/ajouter_etudiant.html", {"form":form, "id":id})

def traitement_update_etudiant(request, id):
    etudiant_existant = models.Etudiants.objects.get(id_etu=id)
    eform = EtudiantForm(request.POST, instance=etudiant_existant)  # Utilisation de instance
    if eform.is_valid():
        etudiant = eform.save()
        return HttpResponseRedirect("/ecole/liste_etudiants")
    else:
        return render(request, "ecole/ajouter_etudiant.html", {"eform": eform, "id": id})

def supprimer_etudiant(request,id):
    etudiant = models.Etudiants.objects.get(id_etu=id)
    etudiant.delete()
    return HttpResponseRedirect("/ecole/liste_etudiants")


#Enseignant
def ajouter_enseignant(request):
    form = EnseignantForm()
    return render(request, "ecole/ajouter_enseignant.html", {"form": form})

def traitement_enseignant(request):
    form = EnseignantForm(request.POST)
    if form.is_valid():
        Enseignant = form.save()
        return HttpResponseRedirect("/ecole/liste_enseignants")
    else:
        return render(request,"ecole/ajouter_enseignant.html/", {"form":form})

def liste_enseignants(request):
    liste_enseignants = list(models.Enseignants.objects.all())
    return render(request, "ecole/liste_enseignants.html", {"liste_en":liste_enseignants})

def afficher_enseignant(request,id):
    enseignant= models.Enseignants.objects.get(id_ens=id)
    return render (request, "ecole/afficher_enseignant.html", {"enseignant": enseignant})

def update_enseignant(request,id):
    enseignant = models.Enseignants.objects.get(id_ens=id)
    dico= enseignant.dico()
    form = EnseignantForm(dico)
    return render(request,"ecole/ajouter_enseignant.html", {"form":form, "id":id})

def traitement_update_enseignant(request, id):
    enseignant_existant = models.Enseignants.objects.get(id_ens=id)
    enform = EnseignantForm(request.POST, instance=enseignant_existant)  # Utilisation de instance
    if enform.is_valid():
        enseignant = enform.save()
        return HttpResponseRedirect("/ecole/liste_enseignants")
    else:
        return render(request, "ecole/ajouter_enseignant.html", {"enform": enform, "id": id})

def supprimer_enseignant(request,id):
    enseignant = models.Enseignants.objects.get(id_ens=id)
    enseignant.delete()
    return HttpResponseRedirect("/ecole/liste_enseignants")

