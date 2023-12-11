N = int(input("Entrez un nombre entier : "))

# Initialisation des variables
somme = 0
moyenne = 0

# Répéter N fois
for i in range(N):
    nombre = int(input("Entrez un nombre : "))
    somme = somme + nombre

moyenne = somme / N

# Afficher la somme et la moyenne
print("La somme est", somme)
print("La moyenne est", moyenne)