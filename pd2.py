#Zadanie 3.2 | Miesiące

#Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.

#Logikę obliczania liczby dni wydziel do osobnej funkcji.

#**Wersja A**
#Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

#A
def przyporzadkuj_nr(miesiac):
    miesiac = input("Podaj miesiac: ")
    slownik = {"styczeń": 1, "luty": 2, "marzec": 3, "kwiecien": 4,"maj": 5,}
    for miesiac, nr_szukany in slownik.items():
        return nr_szukany


przyporzadkuj_nr(miesiac)


liczba_dni_miesiaca = ()
def ile_dni_w_tym_miesiacu(x):
    if nr_szukany % 2 == 0 and nr_szukany < 7:
        liczba_dni_miesiaca = 30
    elif nr_szukany % 2 == 0 and nr_szukany > 9:
        liczba_dni_miesiaca = 31
    else:
        liczba_dni_miesiaca = 31

wynik = ile_dni_w_tym_miesiacu(nr_szukany)
print(wynik)











#**Wersja B (trudniejsza)**
#Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.