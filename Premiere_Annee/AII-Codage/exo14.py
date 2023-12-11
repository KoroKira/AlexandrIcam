# Saisie des données
rayon = float(input("Entrez le rayon du cône : "))
hauteur = float(input("Entrez la hauteur du cône : "))

# Calcul du volume
volume = 3.1415 * (rayon**2) * (hauteur/3)

# Affichage du résultat
print("Le volume du cône est de {:.2f}".format(volume))