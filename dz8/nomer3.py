number = 0

while number !=7:
    number = int(input("Введите число: "))
    if number > 0 and number != 7:
        print("число больше нуля!")
    elif number < 0:
        print("число меньше нуля!")
    elif number == 0:
        print("число равно нулю!")
    else:
        print("Пока!")
        