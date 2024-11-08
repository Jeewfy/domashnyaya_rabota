number = int(input("Введите число которое нужно возвести в степень: "))
degree = int(input("Введите степень: "))
if degree >= 0 and degree < 8:
    print(number ** degree)
else:
    print("Неправильная степень")
