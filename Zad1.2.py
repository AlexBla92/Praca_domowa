data_oddania = str(input("W jaki dzień oddałeś buty do szewca?: "))
trwanie_naprawy = int(input("Ile całkowitych dni będzie trwała naprawa?: "))
if data_oddania == "Poniedziałek":
    data_oddania = 1
elif data_oddania == "Wtorek":
    data_oddania = 2
elif data_oddania == "Środa":
    data_oddania = 3
elif data_oddania == "Czwartek":
    data_oddania = 4
elif data_oddania == "Piątek":
    data_oddania = 5
elif data_oddania == "Sobota":
    data_oddania = 6
elif data_oddania == "Niedziela":
    data_oddania = 7
for data_oddania in range (1,7):
    data_odbioru = data_oddania + trwanie_naprawy
if data_odbioru == 1 or 8:
    print("Poniedziałek")
elif data_odbioru == 2 or 9:
    print("Wtorek")
elif data_odbioru == 3 or 10:
    print("Środa")
elif data_odbioru == 4 or 11:
    print("Czwartek")
elif data_odbioru == 5 or 12:
    print("Piątek")
elif data_odbioru == 6 or 13:
    print("Sobota")
elif data_odbioru == 7 or 14:
    print("Niedziela")
# w każdym przypadku wychodzi mi poniedziałek :(



