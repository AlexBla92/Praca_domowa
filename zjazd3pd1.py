#Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).

#Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.

class Ogloszenie:
    def __init__(self, tytul, opis, dostawa_kurierem, cena, dane_kontaktowe):
        self.tytul = tytul
        self.opis = opis
        self.dostawa_kurierem = dostawa_kurierem
        self.cena = cena
        self.dane_kontaktowe = dane_kontaktowe

    def stworz_ogloszenie(self):
        print(f'{self.tytul}\n{self.opis}\n{self.dostawa_kurierem}\n{self.cena}\n{self.dane_kontaktowe}')

ogloszenie_1 = Ogloszenie("Sprzedam rower", "Sprzedam nieużywaną damkę, 17 cali, beżowa, 5 przerzutek.", "Kurier: tak", "234zł", 791345788)
ogloszenie_1.stworz_ogloszenie()