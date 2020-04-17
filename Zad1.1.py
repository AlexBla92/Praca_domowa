#1
cena_za_1kg=int(input(f"Ile kosztuje kilogram ziemniaków?: "))
koszt_5_kg=cena_za_1kg*5
print(f"Koszt za 5 kg ziemniaków to {koszt_5_kg:.2f} zł")
#2
cena_za_1kg=int(input(f"Ile kosztuje kilogram ziemniaków?: "))
potrzebnailosc=int(input(f"Ile kilogramów chcesz kupić?: "))
koszt=(int(cena_za_1kg)*int(potrzebnailosc))
print("Koszt: ",koszt)
#3
cena_za_1kg_ziemniak=int(input(f"Ile kosztuje kilogram ziemniaków?: "))
potrzebnailosc_ziemniak=int(input(f"Ile kilogramów chcesz kupić?: "))
cena_za_1kg_banan=int(input(f"Ile kosztuje kilogram bananów?: "))
potrzebnailosc_banan=int(input(f"Ile kilogramów chcesz kupić?: "))
kosztziemniaki=cena_za_1kg_ziemniak*potrzebnailosc_ziemniak
kosztbanany=cena_za_1kg_banan*potrzebnailosc_banan
calkowity_koszt=kosztziemniaki+kosztbanany
print("Całkowity koszt to: ",calkowity_koszt)
print(f"Za co zapłacimy więcej?")
if kosztziemniaki<kosztbanany:
    print("Ziemniaki będą tańsze")
else:
    print("Banany będą tańsze")


