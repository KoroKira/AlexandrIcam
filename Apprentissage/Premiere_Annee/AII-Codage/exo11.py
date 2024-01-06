# Saisie du nombre
n = int(input("Veuillez saisir un nombre entier : "))

# Initialisation d'une variable pour le résultat
est_premier = True

# Boucle pour vérifier si N est premier
for i in range(2, n):
  if n % i == 0:
    est_premier = False
    break

# Affichage du résultat
if est_premier:
  print(f"Le nombre {n} est premier.")
else:
  print(f"Le nombre {n} n'est pas premier.")