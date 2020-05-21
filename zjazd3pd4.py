""" klasa Zbiornik posiada dana ilosc wody i korzysta z funkcji sluzacych do dolewania danej ilosc wody
oraz odlewania danej ilosci wody"""
class Zbiornik:
    def __init__(self, ilosc_wody: int):
        self.ilosc_wody = ilosc_wody

    def dolej(self, ile: int):
        self.ilosc_wody = 0
        self.ilosc_wody += ile
        return self.ilosc_wody

    def odlej(self, ile: int):
        if self.ilosc_wody >= ile:
            self.ilosc_wody -= ile
            return self.ilosc_wody
        else:
            print("Nie ma już wody.")

    def __str__(self):
        return f'Zbiornik z {self.ilosc_wody} litrami wody.'


def test_dolej():
    zbiornik_1 = Zbiornik(0)
    assert zbiornik_1.dolej(9) == 9

def test_odlej():
    zbiornik_1 = Zbiornik(9)
    assert zbiornik_1.odlej(2) == 7