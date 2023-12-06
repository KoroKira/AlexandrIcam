def valeurMax(dico):
    max_valeur = 0
    max_cle = ''
    
    for cle, valeur in dico.items():
        if cle != ' ' and valeur > max_valeur:
            max_valeur = valeur
            max_cle = cle
    
    return (max_cle, max_valeur)

# Demander à l'utilisateur de saisir un texte
texte = input("Entrez un texte : ").lower()  # Convertir le texte en minuscules

# Initialiser un dictionnaire pour les occurrences des lettres
occurrences = {}

# Parcourir chaque caractère du texte
for caractere in texte:
    # Mettre à jour le dictionnaire des occurrences pour les caractères alphabétiques
    if caractere.isalpha():
        if caractere in occurrences:
            occurrences[caractere] += 1
        else:
            occurrences[caractere] = 1

# Utiliser la fonction valeurMax pour trouver le caractère le plus fréquent
resultat = valeurMax(occurrences)

if resultat[0] != '':
    print(f"Le caractère le plus fréquent est '{resultat[0]}' avec {resultat[1]} occurrences.")
else:
    print("Aucune lettre alphabétique n'a été trouvée dans le texte.")
