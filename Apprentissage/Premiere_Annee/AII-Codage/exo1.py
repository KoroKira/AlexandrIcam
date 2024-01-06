a=int(input("saisir la valeur majorante"))
b=int(input("saisir la valeur minorante"))
c=int(input("saisir la valeur à vérifier"))

if b<=c<=a :
    print(c, "appartient à l'intervalle entre", b, "et", a)
else:
    print(c, "n'appartient pas à l'intervalle")