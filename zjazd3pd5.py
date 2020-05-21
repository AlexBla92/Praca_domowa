"""
klasa zólw ktora moze zmieniac swoje polozenie i kurs
"""
class Zolw:
    def __init__(self, szerokosc = 100, wysokosc = 100, kurs = 0):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.kurs = kurs

        """
        przesuwanie żółwia o zadane wielkosci 
        """

    def idz(self, x: int, y: int):
        self.szerokosc = 100
        self.szerokosc += x
        self.wysokosc = 100
        self.wysokosc += y

    """obracanie żólwia o zadaną wartosc"""

    def obroc_sie(self, jaki_kurs: int):
        self.kurs = 0
        self.kurs += jaki_kurs

    def __str__(self):
        return f'x = {self.szerokosc}, y= {self.wysokosc}, kurs = {self.kurs}'


z1 = Zolw(100, 100, 0)
z1.idz(50, 10)
print(z1)
z1.obroc_sie(23)
print(z1)

z2 = Zolw(100, 100, kurs = 7)
z2.idz(5, 45)
print(z2)
