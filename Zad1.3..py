wzrost = float(input("Wzrost w m: "))
masa = int(input("Masa ciała w kg: "))
wsp_bmi = int(masa) / float(wzrost)**2
print("Współczynnik BMI to:")
print(wsp_bmi)
if wsp_bmi <= 25:
    print("Nie musisz biegać!")
else:
    wsp_bmi > 25
    print("Rusz się!")
