wiek = int(input("Ile masz lat?: "))
ile_noclegow = int(input("Na ile nocy zostajesz u nas?: "))

if wiek < 18:
    cena = 100
elif wiek in range(18,65) and ile_noclegow == 1:
    cena = 200
elif wiek in range(18,65) and ile_noclegow in range(2,5):
    cena = 180
elif wiek in range(18,65) and ile_noclegow >= 5:
    cena = 150
elif wiek > 64 and ile_noclegow == 1:
    cena = 200*0.9
elif wiek > 64 and ile_noclegow in range(2,5):
    cena = 180*0.9
elif wiek > 64 and ile_noclegow >= 5:
    cena = 150*0.9
print(f"Zapłacisz: {cena * ile_noclegow:.2f}zł.")


