import numpy as np
import matplotlib.pyplot as plt

# Données des différentes groupes
groupes = [1, 2, 3, 4, 5, 6, 7, 8]
c_values = [342, 335, 337, 339, 354, 338, 340, 348]

# Nombre de mesures à faire pour estimer chaque moyenne (simulation de Monte Carlo)
n = 10

# Paramètres pour la simulation
cmoy1 = np.mean(c_values)
uc = np.std(c_values, ddof=1)

# Fonction qui renvoie la moyenne d'une simulation aléatoire de n mesures de célérité
def experience():
    l = []  # liste vide pour sauvegarder les données
    for i in range(n):
        val = np.random.normal(cmoy1, uc)  # tirage aléatoire selon une loi gaussienne centrée en cmoy1 et d'écart-type uc
        l.append(val)
    return np.mean(l)  # moyenne des valeurs de l

# Nombre de simulations
N = 10000

# Liste pour sauvegarder les résultats de simulations
resultats = []

# Effectuer les simulations
for i in range(N):
    moy = experience()
    resultats.append(moy)  # resultats contient les N valeurs de moyennes des n célérités simulées

# Calcul de l'écart-type des moyennes simulées
std_simule = np.std(resultats, ddof=1)

# Calcul de l'incertitude-type par la formule
incertitude_type_formule = uc / np.sqrt(n)

# Affichage des résultats
print(f'Ecart type simulé (avec boucles et listes) = {std_simule:.2f}')
print(f'Incertitude-type par la formule = {incertitude_type_formule:.2f}')

# Affichage de l'histogramme
plt.hist(resultats, bins=50, density=True, alpha=0.75, color='b', label='Moyennes simulées')
plt.axvline(cmoy1, color='r', linestyle='dashed', linewidth=2, label='Célérité moyenne réelle')
plt.axvline(cmoy1 + uc / np.sqrt(n), color='g', linestyle='dashed', linewidth=2, label='Incertitude-type')
plt.axvline(cmoy1 - uc / np.sqrt(n), color='g', linestyle='dashed', linewidth=2)

plt.title("Histogramme des moyennes simulées")
plt.xlabel("Célérité (m/s)")
plt.ylabel("Fréquence")
plt.legend()
plt.show()
