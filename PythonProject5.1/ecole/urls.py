from django.urls import path
from . import views

urlpatterns = [
    # Index/page d'accueil
    path("", views.index, name="index"),

    #CRUD groupes
    path("ajouter_groupe/", views.ajouter_groupe, name="ajouter_groupe"),
    path("traitement_groupe/",views.traitement_groupe,name="traitement_groupe"),
    path("liste_groupes/",views.liste_groupes,name="liste_groupes"),
    path("afficher_groupe/<int:id>/", views.afficher_groupe),
    path("update_groupe/<int:id>/",views.update_groupe),
    path("traitement_update_groupe/<int:id>/",views.traitement_update_groupe),
    path("supprimer_groupe/<int:id>/",views.supprimer_groupe),

    #CRUD etudiants
    path("ajouter_etudiant/", views.ajouter_etudiant, name="ajouter_etudiant"),
    path("traitement_etudiant/",views.traitement_etudiant,name="traitement_etudiant"),
    path("liste_etudiants/",views.liste_etudiants,name="liste_etudiants"),
    path("afficher_etudiant/<int:id>/", views.afficher_etudiant),
    path("update_etudiant/<int:id>/",views.update_etudiant),
    path("traitement_update_etudiant/<int:id>/",views.traitement_update_etudiant),
    path("supprimer_etudiant/<int:id>/",views.supprimer_etudiant),

    #CRUD enseignants
    path("ajouter_enseignant/", views.ajouter_enseignant, name="ajouter_enseignant"),
    path("traitement_enseignant/",views.traitement_enseignant,name="traitement_enseignant"),
    path("liste_enseignants/",views.liste_enseignants,name="liste_enseignants"),
    path("afficher_enseignant/<int:id>/", views.afficher_enseignant),
    path("update_enseignant/<int:id>/",views.update_enseignant),
    path("traitement_update_enseignant/<int:id>/",views.traitement_update_enseignant),
    path("supprimer_enseignant/<int:id>/",views.supprimer_enseignant),

    #CRUD enseignants
    path("ajouter_cours/", views.ajouter_cours, name="ajouter_cours"),
    path("traitement_cours/",views.traitement_cours,name="traitement_cours"),
    path("liste_cours/",views.liste_cours,name="liste_cours"),
    path("afficher_cours/<int:id>/",views.afficher_cours,name="afficher_cours"),
    path("update_cours/<int:id>/",views.update_cours),
    path("traitement_update_cours/<int:id>/",views.traitement_update_cours,name="traitement_update_cours"),
    path("supprimer_cours/<int:id>/",views.supprimer_cours),

    #CRUD absences
    path("ajouter_absence/", views.ajouter_absence, name="ajouter_absence"),
    path("traitement_absence/",views.traitement_absence,name="traitement_absence"),
    path("liste_absences/",views.liste_absences,name="liste_absences"),
    path("afficher_absence/<int:id>/", views.afficher_absence),
    path("update_absence/<int:id>/",views.update_absence),
    path("traitement_update_absence/<int:id>/",views.traitement_update_absence),
    path("supprimer_absence/<int:id>/",views.supprimer_absence),


    path('etudiant/<int:etudiant_id>/absences/', views.fiche_absence, name='fiche_absence'),
    path('cours/<int:cours_id>/absences/', views.liste_absences_cours, name='liste_absences_cours'),

]