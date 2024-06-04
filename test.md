# Exercices Résolus avec Explications

J'ai résolu pour toi les exercices et je vais t'expliquer tout ça dans ce fichier. On va passer en revue chaque exercice ensemble.

## Exercice 10 : Correction de la Fonction `dichotomie`


```python
def dichotomie(f, a, b, eps):
    while (b - a) > eps:
        m = (a + b) / 2
        if f(a) * f(m) < 0: 
            b = m
        else:
            a = m
    return (a + b) / 2
```

## Exercice 11 : Vérification de la Primalité

1. Pour tester si un nombre est premier, on peut utiliser une liste de nombres premiers. Voici la fonction `testi` :

```python
def testi(n):
    premiers = [2, 3, 5, 7, 11, 13, 17]  # Liste de nombres premiers
    return n in premiers
```

2. J'ai corrigé et amélioré la fonction `premier` comme suit :

```python
def premier(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True
```

3. La fonction `test2` teste maintenant tous les nombres non premiers entre 0 et 10 inclus :

```python
def test2():
    for i in range(11):
        if not premier(i):
            print(i, "n'est pas premier.")
```

4. J'ai ajouté une optimisation dans la fonction `premier` pour parcourir les diviseurs jusqu'à la racine carrée de `n`. Cela rend la fonction plus efficace. Pour t'expliquer la différence, initialement tu avais for d in range (2,n), et ici c'est for d in range(2, int(n**0.5) + 1). Ça permet globalement d'être plus précis dans ton calcul, car n devient la racine carré de n auquel on ajoute 1. Fin bref, c'est des maths, et bah, c'est ça qui est attendu
