import os

dossier_courant = os.path.dirname(__file__)

chemin_liste_course = os.path.join(dossier_courant, "liste.json")

if(os.path.exists(chemin_liste_course)):
    with open(chemin_liste_course, "r") as f:
        liste_course = json.load(f)
else:
    liste_de_course = []

affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""
choix = "0"

while(choix != "5"):
    choix = input(affichage)