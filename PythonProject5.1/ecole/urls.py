from django.urls import path
from . import views

urlpatterns = [
    # Index/page d'accueil
    path("", views.index, name="index"),
    path("ajouter_groupe/", views.ajouter_groupe, name="ajouter_groupe"),
    path("traitement_groupe/",views.traitement_groupe,name="traitement_groupe"),
    path("liste_groupes/",views.liste_groupes,name="liste_groupes"),
    path("afficher_groupe/<int:id>/", views.afficher_groupe),
    path("update_groupe/<int:id>/",views.update_groupe),
    path("traitement_update_groupe/<int:id>/",views.traitement_update_groupe),
    path("supprimer_groupe/<int:id>/",views.supprimer_groupe),
]