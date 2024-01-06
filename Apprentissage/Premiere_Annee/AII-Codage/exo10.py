# Définition des variables
a = int(input("Entrez un entier : "))
b = int(input("Entrez un deuxième entier : "))

# Initialisation du produit et du compteur
produit = 0
compteur = 0

# Boucle pour additionner a autant de fois que b
while compteur < b:
    produit += a
    compteur += 1

# Affichage du résultat
print("Le produit des deux entiers est :", produit)