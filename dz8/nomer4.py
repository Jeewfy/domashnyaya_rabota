summa = 0
number = int(input("Введите число: "))
maximum = number
minimum = number

while number != 7:
    number = int(input("Введите число: "))
    summa += number
    if number == 7:
        print("Пока!")
        break
    elif number < minimum:
        minimum = number
    elif number > maximum:
        maximum = number
      
    print(f"Сумма: {summa}", f"Макс: {maximum}", f"Мин: {minimum}")