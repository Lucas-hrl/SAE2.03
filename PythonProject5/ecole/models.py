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

    def __str__(self):
        return self.nom_gr

    class Meta:
        managed = True
        db_table = 'groupe'


class Etudiants(models.Model):
    id_etu = models.AutoField(primary_key=True)
    nom_etu = models.CharField(max_length=100)
    prenom_etu = models.CharField(max_length=100)
    mail_etu = models.EmailField(unique=True, max_length=150)
    groupe = models.ForeignKey(Groupe, models.DO_NOTHING, db_column='groupe', blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom_etu} {self.nom_etu}"

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

    class Meta:
        managed = True
        db_table = 'enseignants'


class Cours(models.Model):
    id_cours = models.AutoField(primary_key=True)
    titre_cours = models.CharField(max_length=150)
    date_cours = models.DateField()
    enseignants = models.ForeignKey(Enseignants, models.DO_NOTHING, db_column='enseignants', blank=True, null=True)
    groupe = models.ForeignKey(Groupe, models.DO_NOTHING, db_column='groupe', blank=True, null=True)
    duree_cours = models.TimeField(blank=True, null=True)

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

    class Meta:
        managed = True
        db_table = 'absences'
