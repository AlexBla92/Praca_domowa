from ab_oop.zjazd3pd1 import Ogloszenie

class Ogloszenie_samochodowe(Ogloszenie):
    def __init__(self, tytul, opis, dostawa_kurierem, cena, dane_kontaktowe, model, marka, rok_produkcji, przebieg, pojemnosc, moc, rodzaj_paliwa):
        super().__init__(tytul, opis, dostawa_kurierem, cena, dane_kontaktowe)
        self.model = model
        self.marka = marka
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
        self.pojemnosc = pojemnosc
        self.moc = moc
        self.rodzaj_paliwa = rodzaj_paliwa

class Ogloszenie_mieszkaniowe(Ogloszenie):
    def __init__(self, tytul, opis, dostawa_kurierem, cena, dane_kontaktowe, miejscowosc, metraz, liczba_pokoi):
        super().__init__(tytul, opis, dostawa_kurierem, cena, dane_kontaktowe)
        self.miejscowosc = miejscowosc
        self.metraz = metraz
        self.liczba_pokoi = liczba_pokoi

    def stworz_ogloszenie(self):
        print(f'{self.tytul}\n{self.opis}\n{self.dostawa_kurierem}\n{self.cena}\n{self.dane_kontaktowe}\n{self.miejscowosc}\n{self.metraz}\n{self.liczba_pokoi}')


ogloszenie_2 = Ogloszenie_mieszkaniowe("Dom", "Ladny dom", "15 0005zl", "ja", "Ul", "Warszawa", "15", 4)
ogloszenie_2.stworz_ogloszenie()