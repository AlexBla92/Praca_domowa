wiek = int(input("Ile masz lat?: "))
ilosc = int(input("Ile biletów potrzebujesz?: "))
if wiek in range(0-7):
    cena = 0
elif wiek in range(7,18):
    cena = 2.28
elif wiek in range(18,65):
    cena = 3.80
elif wiek > 65:
    cena = 1.90
koszt_biletow = cena*ilosc
print(f'Za bilety zapłacisz {koszt_biletow:.2f}zł.')