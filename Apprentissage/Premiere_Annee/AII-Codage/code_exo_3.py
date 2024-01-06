def troisValeursMax(dico):
    valeurs_triees = sorted(dico.items(), key=lambda x: x[1], reverse=True)
    valeurs_max = []

    for cle, valeur in valeurs_triees:
        if cle != ' ':
            valeurs_max.append((cle, valeur))
        if len(valeurs_max) == 3:
            break

    return valeurs_max

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

# Utiliser la fonction troisValeursMax pour trouver les trois caractères les plus fréquents
resultat = troisValeursMax(occurrences)

if resultat:
    print("Les trois caractères les plus fréquents sont :")
    for cle, valeur in resultat:
        print(f"'{cle}' avec {valeur} occurrences.")
else:
    print("Aucune lettre alphabétique n'a été trouvée dans le texte.")
