def interaktywna_metoda_falsi():
    """
    Interaktywna wersja metody falsi z możliwością wprowadzania własnych przedziałów.
    """
    import math

    # Definiujemy funkcję
    def f(x):
        return x ** 3 - x - 2

    print("Metoda falsi (regula falsi) - znajdowanie miejsca zerowego")
    print("Funkcja: f(x) = x^3 - x - 2")

    while True:
        try:
            a = float(input("\nPodaj początek przedziału a: "))
            b = float(input("Podaj koniec przedziału b: "))

            if f(a) * f(b) >= 0:
                print(f"Błąd: f({a}) = {f(a)} i f({b}) = {f(b)} mają ten sam znak!")
                print("Spróbuj ponownie z innym przedziałem.")
                continue

            tolerancja = float(input("Podaj tolerancję (np. 1e-6): "))

            wynik = metoda_falsi(f, a, b, tolerancja)
            if wynik is not None:
                print(f"\nZnalezione miejsce zerowe: {wynik}")
                print(f"Wartość funkcji w tym punkcie: {f(wynik)}")

            kont = input("\nCzy chcesz sprawdzić inny przedział? (t/n): ").lower()
            if kont != 't':
                break

        except ValueError:
            print("Błąd: Wprowadź poprawne liczby!")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    interaktywna_metoda_falsi()