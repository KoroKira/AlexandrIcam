def equation(x):
    return x**3 - 3*x**2 - 9*x + 15

def dichotomie(a, b, epsilon):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if equation(a) * equation(c) < 0:
            b = c
        else:
            a = c
    return round(a, 3), round(b, 3)  # Arrondir les valeurs à 3 décimales

a = -1
b = 3
epsilon = 1e-3

solution_a, solution_b = dichotomie(a, b, epsilon)

print("L'encadrement de la solution est :", solution_a, solution_b)
