# Étape 1 : Demander à l'utilisateur de saisir un texte
texte = input("Entrez un texte : ").lower()  # Convertir le texte en minuscules

# Étape 2 : Initialiser un dictionnaire pour les occurrences des lettres
dic = {}

# Étape 3 : Parcourir chaque caractère du texte qui a été input par l'utilisateur
for caractere in texte:
    # Étape 4 : Mettre à jour le dictionnaire des occurrences pour les caractères alphabétiques => lire un caractère, et ajouter "1pt" à chaque lettre si elle réapparait
    if caractere.isalpha():
        if caractere in dic:
            dic[caractere] += 1
        else:
            dic[caractere] = 1

# Étape 5 : Afficher les résultats en print, donc ça liste une lettre et ca regarde le chiffre associé dans le dictionnaire, jusqu'à ce que toute les lettres soient listées
print("Occurrences des lettres :")
for lettre, nombre in dic.items():
    print(f"{lettre}={nombre}, ", end="")
