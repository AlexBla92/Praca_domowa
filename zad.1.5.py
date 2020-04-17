#Z boków o danych długościach a,b i c można utworzyć trójkąt gdy:
#a+b>c
#a+c>b
#b+c>a
a = int(input("Pierwszy bok ma: "))
b = int(input("Drugi bok ma: "))
c = int(input("Podstawa ma: "))
if not (a + b) > c and (a + c) > b and (b + c) > a:
    print("Nie da się utworzyć trójkąta.")
else:
    polowa_obwodu = (a+b+c)/2
import math
pole = math.sqrt(polowa_obwodu(polowa_obwodu-c)(polowa_obwodu-b)(polowa_obwodu-a))
print("Pole trójkąta wynosi: {pole}cm3")
#pojawia się problem float object is not callable
# nie działaja mi tez skroty w pycharmie takie jak shift ctr 10 etc





