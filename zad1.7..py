produkt = str(input("Co chcesz kupić?:  "))
ilosc = float(input("W jakiej ilości?: "))
cena = float(input("Ile kosztuje produkt?: "))
koszt = cena * ilosc
print(f"Zapłacisz: {koszt:2f} zł") #jak sprawić, żeby wynik nie wychodził w formie 00.00000000 tylko 00.00?