# on demande à l'utilisateur d'entrer un nombre entier positif
nombre = int(input("Entrez un nombre entier positif : "))

# initialisation de la variable de comptage
compteur = 0

# tant que le nombre est divisible par 2
while nombre % 2 == 0:
    # on incrémente le compteur
    compteur += 1
    # on divise le nombre par 2
    nombre //= 2

# on affiche le résultat
print("Le nombre est divisible par 2", compteur, "fois.")