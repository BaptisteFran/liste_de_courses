import os

dossier_courant = os.path.dirname(__file__)

chemin_liste_course = os.path.join(dossier_courant, "liste.json")

if(os.path.exists(chemin_liste_course)):
    with open(chemin_liste_course, "r") as f:
        liste_course = json.load(f)
else:
    liste_de_course = []