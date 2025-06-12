from django import forms
from .models import Groupe, Etudiants, Enseignants, Cours, Absences

class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['nom_gr']
        labels = {'nom_gr': 'Nom du groupe'}

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiants
        fields = ['nom_etu', 'prenom_etu', 'mail_etu', 'groupe', 'photo']
        labels = {
            'nom_etu': 'Nom',
            'prenom_etu': 'Prénom',
            'mail_etu': 'E-mail',
            'groupe': 'Groupe',
            'photo': 'Photo'
        }

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignants
        fields = ['nom_ens', 'prenom_ens', 'mail_ens']
        labels = {
            'nom_ens': 'Nom',
            'prenom_ens': 'Prénom',
            'mail_ens': 'E-mail'
        }

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['titre_cours', 'date_cours', 'enseignants', 'groupe', 'duree_cours']
        labels = {
            'titre_cours': 'Titre',
            'date_cours': 'Date',
            'enseignants': 'Enseignant',
            'groupe': 'Groupe',
            'duree_cours': 'Durée'
        }

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absences
        fields = ['etudiants', 'cours', 'justifie', 'justification']
        labels = {
            'etudiants': 'Étudiant',
            'cours': 'Cours',
            'justifie': 'Justifié',
            'justification': 'Justification'
        }
