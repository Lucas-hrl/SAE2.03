from django import forms
from .models import Groupe, Etudiants, Enseignants, Cours, Absences

class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['nom_gr']
        labels = {'nom_gr': 'Nom du groupe'}

        widgets = {
            'nom_gr': forms.TextInput(attrs={'class': 'class_css_input', 'placeholder': 'Nom du groupe…'}),
        }

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

        widgets = {
            'nom_etu': forms.TextInput(attrs={'class': 'class_css_input', "placeholder': 'Nom de l'étudiant…"}),
            'prenom_etu': forms.TextInput(attrs={'class': 'class_css_input', "placeholder': 'Prénom de l'étudiant…"}),
            'mail_etu': forms.EmailInput(),
            'groupe': forms.Select(attrs={'class': 'class_css_input'}),
            'photo': forms.FileInput(attrs={'class': 'class_css_input'}),
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
        widgets = {
            'nom_ens': forms.TextInput(attrs={'class': 'class_css_input', "placeholder': 'Nom de l'enseignant…"}),
            'prenom_ens': forms.TextInput(attrs={'class': 'class_css_input', "placeholder': 'Prénom de l'enseignant…"}),
            'mail_ens': forms.EmailInput(),
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
        widgets = {
            'titre_cours': forms.TextInput(attrs={'class': 'class_css_input', "placeholder': 'Titre du cours…"}),
            'date_cours': forms.DateInput(),
            'enseignants': forms.Select(attrs={'class': 'class_css_input'}),
            'groupe': forms.Select(attrs={'class': 'class_css_input'}),
            'duree_cours': forms.TimeInput(),
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
        widgets = {
            'etudiants':forms.Select(attrs={'class': 'class_css_input'}),
            'cours':forms.Select(attrs={'class': 'class_css_input'}),
            'justifie':forms.CheckboxInput(),
            'justification':forms.FileInput(attrs={'class': 'class_css_input'}),
        }
