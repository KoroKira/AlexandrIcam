n = int(input("Entrez un nombre entier : ")) # Demander à l'utilisateur d'entrer un nombre entier

fact = 1 # Initialiser la variable fact à 1

if n < 0: # Si le nombre est négatif
    print("Erreur - nombre négatif!") # Afficher un message d'erreur

elif n == 0: # Si le nombre est 0
    print("Le factoriel de 0 est 1") # Afficher un message

else: # Si le nombre est positif
    for i in range(1,n+1): # Pour i allant de 1 à n+1
        fact = fact*i # Le facteur est égal à sa valeur précédente multipliée par i
    print("Le factoriel de",n,"est",fact) # Afficher le facteur