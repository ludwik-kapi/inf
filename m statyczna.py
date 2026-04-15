def f(x):
    return x ** 2 - 4 * x - 4


def df(x):
    return 2 * x - 4


def newton(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        print(f"Iteracja {i + 1}: x = {x_new}")

        if abs(x_new - x) < tol:
            return x_new

        x = x_new
    return x


wynik = newton(3)
print("Wynik:", wynik)