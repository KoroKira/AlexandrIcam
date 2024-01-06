# Demande à l'utilisateur de saisir un entier
n = int(input("Saisissez un entier :"))
 
# Initialisation de la somme à 0
sum = 0
 
# Pour chaque diviseur de n
for i in range(1, n):
    if n % i == 0:
        sum += i
 
# Vérifie si la somme est égale à l'entier saisi
if sum == n:
    print(n, "est parfait")
else:
    print(n, "n'est pas parfait")