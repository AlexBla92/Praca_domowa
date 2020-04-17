liczba = 0
for liczba in range(1,101):
    if liczba % 3 == 0 and liczba % 15 != 0:
        print(f"{liczba} Fizz")
    elif liczba % 5 == 0 and liczba % 15 != 0:
        print(f"{liczba} Buzz")
    elif liczba % 15 == 0:
        print(f"{liczba} FizzBuzz")
    else:
        print(liczba)
    liczba += 1