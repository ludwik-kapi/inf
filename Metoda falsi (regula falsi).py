def f(x):
    return x ** 2 - 4 * x - 4


def falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Zły przedział!")
        return None

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"Iteracja {i + 1}: x = {c}")

        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c


wynik = falsi(0, 5)
print("Wynik:", wynik)