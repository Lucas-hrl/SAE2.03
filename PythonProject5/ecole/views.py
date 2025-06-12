from .models import Groupe, Etudiants, Enseignants, Cours, Absences
from .forms import GroupeForm, EtudiantForm, EnseignantForm, CoursForm, AbsenceForm

# Groupes
def liste_groupes(request):
    groupes = Groupe.objects.all()
    return render(request, 'ecole/liste_groupes.html', {'groupes': groupes})

def ajouter_groupe(request):
    if request.method == 'POST':
        form = GroupeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_groupes')
    else:
        form = GroupeForm()
    return render(request, 'ecole/ajouter_groupe.html', {'form': form})

def modifier_groupe(request, pk):
    groupe = get_object_or_404(Groupe, pk=pk)
    if request.method == 'POST':
        form = GroupeForm(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            return redirect('liste_groupes')
    else:
        form = GroupeForm(instance=groupe)
    return render(request, 'ecole/modifier_groupe.html', {'form': form, 'groupe': groupe})

def supprimer_groupe(request, pk):
    groupe = get_object_or_404(Groupe, pk=pk)
    if request.method == 'POST':
        groupe.delete()
        return redirect('liste_groupes')
    return render(request, 'ecole/supprimer_groupe.html', {'groupe': groupe})

# Étudiants
def liste_etudiants(request):
    etudiants = Etudiants.objects.all()
    return render(request, 'ecole/liste_etudiants.html', {'etudiants': etudiants})

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'ecole/ajouter_etudiant.html', {'form': form})

def modifier_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiants, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'ecole/modifier_etudiant.html', {'form': form, 'etudiant': etudiant})

def supprimer_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiants, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'ecole/supprimer_etudiant.html', {'etudiant': etudiant})

# Enseignants
def liste_enseignants(request):
    enseignants = Enseignants.objects.all()
    return render(request, 'ecole/liste_enseignants.html', {'enseignants': enseignants})

def ajouter_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm()
    return render(request, 'ecole/ajouter_enseignant.html', {'form': form})

def modifier_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignants, pk=pk)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'ecole/modifier_enseignant.html', {'form': form, 'enseignant': enseignant})

def supprimer_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignants, pk=pk)
    if request.method == 'POST':
        enseignant.delete()
        return redirect('liste_enseignants')
    return render(request, 'ecole/supprimer_enseignant.html', {'enseignant': enseignant})


# Absences
def liste_absences(request):
    absences = Absences.objects.all()
    return render(request, 'ecole/liste_absences.html', {'absences': absences})

def ajouter_absence(request):
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_absences')
    else:
        form = AbsenceForm()
    return render(request, 'ecole/ajouter_absence.html', {'form': form})

def modifier_absence(request, pk):
    absence = get_object_or_404(Absences, pk=pk)
    if request.method == 'POST':
        form = AbsenceForm(request.POST, instance=absence)
        if form.is_valid():
            form.save()
            return redirect('liste_absences')
    else:
        form = AbsenceForm(instance=absence)
    return render(request, 'ecole/modifier_absence.html', {'form': form, 'absence': absence})

def supprimer_absence(request, pk):
    absence = get_object_or_404(Absences, pk=pk)
    if request.method == 'POST':
        absence.delete()
        return redirect('liste_absences')
    return render(request, 'ecole/supprimer_absence.html', {'absence': absence})


import csv

def import_absences(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        decoded = csv_file.read().decode("utf-8").splitlines()
        reader = csv.reader(decoded)
        for row in reader:
            Absences.objects.create(
                etudiants_id=int(row[0]),  # id_etu
                cours_id=int(row[1]),      # id_cours
                justifie=int(row[2]),      # 0 ou 1
                justification=row[3]       # texte
            )
        return redirect('liste_absences')
    return render(request, 'ecole/import_absences.html')

# Fiche d’un cours
def fiche_absences_cours(request, id_cours):
    absences = Absences.objects.filter(cours_id=id_cours)
    return render(request, 'ecole/fiche_absences_cours.html', {'absences': absences})

# Fiche d’un étudiant
def fiche_absences_etudiant(request, id_etu):
    absences = Absences.objects.filter(etudiants_id=id_etu)
    total_justifiees = absences.filter(justifie=1).count()
    total_non_justifiees = absences.filter(justifie=0).count()
    return render(request, 'ecole/fiche_absences_etudiant.html', {
        'absences': absences,
        'total_justifiees': total_justifiees,
        'total_non_justifiees': total_non_justifiees
    })
