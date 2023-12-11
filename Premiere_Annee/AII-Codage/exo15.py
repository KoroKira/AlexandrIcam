taux_TVA = int(input("Quel est le taux de la TVA ? Donner la valeur en chiffre seulement, ex. 20.0 (valeurs possibles: 20%, 10%, 5.5%, 2.1%)"))

prix_HT = input('Entrez un prix HT (entrez "o" pour terminer): ')

while prix_HT != 'o':
    prix_HT = float(prix_HT)
    prix_TTC = prix_HT + (prix_HT * taux_TVA / 100)
    print('Le prix TTC est de :{:.2f}'.format(prix_TTC))
    prix_HT = input('Entrez un prix HT (entrez "o" pour terminer): ')