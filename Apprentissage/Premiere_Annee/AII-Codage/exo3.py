h=int(input("Combien d'heures as tu travaillé ?"))
i=float(input("Quel est ton salaire horaire ?"))
o=h-39

if o==0:
    print("Ta paye d'heure sup est nulle")

elif 1<=o<=5:
    print(1.5*i*o, "€ sera ta paye d'heure sup")

elif 6<=o<=10:
    print(1.75*i*o, "€ sera ta paye d'heure sup")

else:
    print(i*2*o, "€ sera ta paye d'heure sup")