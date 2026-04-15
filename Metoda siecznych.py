def f(x):
    return x ** 2 - 4 * x - 4


def sieczne(x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Iteracja {i + 1}: x = {x2}")

        if abs(x2 - x1) < tol:
            return x2

        x0, x1 = x1, x2

    return x2


# przykład
wynik = sieczne(0, 5)
print("Wynik:", wynik)