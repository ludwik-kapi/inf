

import sympy as sp

def metoda_stycznych():
    x = sp.Symbol('x')

    wyrazenie = input("Podaj funkcję f(x) (np. x**3 - x - 2): ")
    f = sp.sympify(wyrazenie)
    df = sp.diff(f, x)

    x0 = float(input("Podaj punkt startowy x0: "))
    epsilon = float(input("Podaj dokładność epsilon (np. 1e-7): "))
    max_iter = int(input("Podaj maksymalną liczbę iteracji: "))

    print(f"\nPochodna: {df}\n")

    x_n = x0

    for i in range(max_iter):
        f_val = float(f.subs(x, x_n))
        df_val = float(df.subs(x, x_n))

        if df_val == 0:
            print("Pochodna równa 0 — metoda nie może kontynuować.")
            return None

        x_next = x_n - f_val / df_val

        print(f"Iteracja {i+1}: x = {x_next}")

        if abs(x_next - x_n) < epsilon:
            print(f"\nPrzybliżony pierwiastek: {x_next}")
            return x_next

        x_n = x_next

    print("\nNie osiągnięto dokładności w zadanej liczbie iteracji.")
    return None

metoda_stycznych()