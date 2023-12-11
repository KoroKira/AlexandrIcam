# Lecture de la note
note = int(input("Entrez votre note : "))

# Calculer la mention correspondante
if note < 0 or note > 20:
    print("Erreur : note invalide !")
elif note == 20:
    print("Mention : Excellent !")
elif note >= 16:
    print("Mention : Très bien !")
elif note >= 14:
    print("Mention : Bien !")
elif note >= 12:
    print("Mention : Assez bien !")
elif note >= 10:
    print("Mention : Passable !")
else:
    print("Mention : Insuffisant !")