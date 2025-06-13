# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import EmailValidator

class Groupe(models.Model):
    id_gr = models.AutoField(primary_key=True)
    nom_gr = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.id_gr:
            max_id = Groupe.objects.all().aggregate(models.Max('id_gr'))['id_gr__max']
            self.id_gr = 1 if max_id is None else max_id + 1
        super(Groupe, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom_gr

    class Meta:
        managed = True
        db_table = 'groupe'

    def dico(self):
        return {
            'id_gr': self.id_gr,
            'nom_gr': self.nom_gr
        }


class Etudiants(models.Model):
    id_etu = models.AutoField(primary_key=True)
    nom_etu = models.CharField(max_length=100)
    prenom_etu = models.CharField(max_length=100)
    mail_etu = models.EmailField(unique=True, max_length=150)
    groupe = models.ForeignKey(Groupe, models.DO_NOTHING, db_column='groupe', blank=True, null=True)
    photo = models.ImageField(upload_to="etudiants/", blank=True, null=True)

    def __str__(self):
        return f"{self.prenom_etu} {self.nom_etu}"

    def save(self, *args, **kwargs):
        if not self.id_etu:
            max_id = Etudiants.objects.all().aggregate(models.Max('id_etu'))['id_etu__max']
            self.id_etu = 1 if max_id is None else max_id + 1
        super(Etudiants, self).save(*args, **kwargs)

    def dico(self):
        return {
            'id_etu': self.id_etu,
            'nom_etu': self.nom_etu,
            'prenom_etu': self.prenom_etu,
            'mail_etu': self.mail_etu,
            'groupe': self.groupe.dico() if self.groupe else None,
            'photo': self.photo
        }

    class Meta:
        managed = True
        db_table = 'etudiants'


class Enseignants(models.Model):
    id_ens = models.AutoField(primary_key=True)
    nom_ens = models.CharField(max_length=100)
    prenom_ens = models.CharField(max_length=100)
    mail_ens = models.EmailField(unique=True, max_length=150)

    def __str__(self):
        return f"{self.prenom_ens} {self.nom_ens}"

    def save(self, *args, **kwargs):
        if not self.id_ens:
            max_id = Enseignants.objects.all().aggregate(models.Max('id_ens'))['id_ens__max']
            self.id_ens = 1 if max_id is None else max_id + 1
        super(Enseignants, self).save(*args, **kwargs)

    def dico(self):
        return {
            'id_ens': self.id_ens,
            'nom_ens': self.nom_ens,
            'prenom_ens': self.prenom_ens,
            'mail_ens': self.mail_ens
        }

    class Meta:
        managed = True
        db_table = 'enseignants'


class Cours(models.Model):
    id_cours = models.AutoField(primary_key=True)
    titre_cours = models.CharField(max_length=150)
    date_cours = models.DateField()
    enseignants = models.ForeignKey(Enseignants, models.DO_NOTHING, db_column='enseignants', blank=True, null=True)
    groupe = models.ForeignKey(Groupe, models.DO_NOTHING, db_column='groupe', blank=True, null=True)
    duree_cours = models.DurationField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id_cours:
            max_id = Cours.objects.all().aggregate(models.Max('id_cours'))['id_cours__max']
            self.id_cours = 1 if max_id is None else max_id + 1
        super(Cours, self).save(*args, **kwargs)

    def dico(self):
        return {
            'id_cours': self.id_cours,
            'titre_cours': self.titre_cours,
            'date_cours': self.date_cours,
            'enseignants': self.enseignants.dico() if self.enseignants else None,
            'groupe': self.groupe.dico() if self.groupe else None,
            'duree_cours': self.duree_cours
        }

    def __str__(self):
        return f"{self.titre_cours} - {self.date_cours}"

    class Meta:
        managed = True
        db_table = 'cours'


class Absences(models.Model):
    id_absence = models.AutoField(primary_key=True)
    etudiants = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='etudiants', blank=True, null=True)
    cours = models.ForeignKey(Cours, models.DO_NOTHING, db_column='cours', blank=True, null=True)
    justifie = models.IntegerField(blank=True, null=True)
    justification = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Absence de {self.etudiants} au cours {self.cours}"

    def save(self, *args, **kwargs):
        if not self.id_absence:
            max_id = Absences.objects.all().aggregate(models.Max('id_absence'))['id_absence__max']
            self.id_absence = 1 if max_id is None else max_id + 1
        super(Absences, self).save(*args, **kwargs)

    def dico(self):
        return {
            'id_absence': self.id_absence,
            'etudiants': self.etudiants.dico() if self.etudiants else None,
            'cours': self.cours.dico() if self.cours else None,
            'justification': self.justification,
            'justifie': self.justifie,
        }

    class Meta:
        managed = True
        db_table = 'absences'
