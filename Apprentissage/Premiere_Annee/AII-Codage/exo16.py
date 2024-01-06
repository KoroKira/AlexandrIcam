nombre = int(input("Entrez un nombre : "))

somme = 0
nombres_sup_100 = 0
nombre_de_donnees = 0

while nombre > 0:
    somme += nombre
    nombre_de_donnees += 1
    if nombre > 100:
        nombres_sup_100 += 1
    nombre = int(input("Entrez un nombre : "))

print("La somme des nombres est :", somme)
print("Il y a eu", nombre_de_donnees, "données et", nombres_sup_100, "d'entre elles étaient supérieures à 100.")