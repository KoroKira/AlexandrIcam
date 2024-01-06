# Initialisation
notes = []
total = 0

# Saisie des notes
note_saisie = float(input("Entrez une note (note négative pour quitter): "))
while note_saisie >= 0:
    notes.append(note_saisie)
    total += note_saisie
    note_saisie = float(input("Entrez une autre note (note négative pour quitter): "))

# Calcul et affichage de la moyenne
moyenne = total / len(notes)
print("Moyenne de ces " + str(len(notes)) + " notes : " + str(moyenne))