# Zadanie 1 – Python
# Autor: [Dawid Kozioł]
# Cel: użycie funkcji wbudowanej, modułu standardowego i obsługi wyjątku

# Dokumentacja funkcji wbudowanej zip():
# https://docs.python.org/3/library/functions.html#zip

# Dokumentacja modułu random:
# https://docs.python.org/3/library/random.html

# Dokumentacja wyjątku ValueError:
# https://docs.python.org/3/library/exceptions.html#ValueError

# Import modułu standardowego 'random'
import random

# Tworzymy dwie listy:
# - lista nazw produktów
# - lista odpowiadających im cen
produkty = ["Mleko", "Chleb", "Ser"]
ceny = [4.5, 3.0, 7.2]

# Funkcja zip() łączy listy w pary (produkt, cena)
# np. zip(["Mleko", "Chleb"], [4.5, 3.0]) -> [("Mleko", 4.5), ("Chleb", 3.0)]
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip
lista_par = list(zip(produkty, ceny))
print("Produkty i ceny:", lista_par)

# Używamy funkcji random.uniform(), aby wylosować rabat procentowy
# np. random.uniform(5, 30) -> losowa liczba z przedziału 5–30
# Dokumentacja: https://docs.python.org/3/library/random.html#random.uniform
znizka = random.uniform(5, 30)
print(f"Promocja! Rabat: {znizka:.2f}%")

# Obsługa błędów – jeśli użytkownik wpisze coś innego niż liczba
# przykład błędu: int("abc") -> ValueError
# Dokumentacja: https://docs.python.org/3/library/exceptions.html#ValueError
try:
    sztuki = int(input("Podaj liczbę sztuk każdego produktu: "))
    laczna_cena = sum(ceny) * sztuki * (1 - znizka / 100)
    print(f"Łączna cena po rabacie: {laczna_cena:.2f} zł")
except ValueError:
    print("Błąd: Podano nieprawidłową wartość (nie liczbę).")
