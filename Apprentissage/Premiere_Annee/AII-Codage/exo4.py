# Lecture des données
heure = int(input("Entrez l'heure : "))
minutes = int(input("Entrez les minutes : "))

# Calculer l'heure et les minutes qui viennent
minutes += 1
if minutes == 60:
    heure += 1
    minutes = 0

if heure == 24:
    heure = 0

# Afficher le résultat
print("Il sera", heure, "heures et", minutes, "minutes.")