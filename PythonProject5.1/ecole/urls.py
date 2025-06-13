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


]