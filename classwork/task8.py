k = int(input("Введите день года: "))
if k % 7 == 0:
    print("Если год начинается с пн")
elif (k - 1) % 7 == 0:
    print("Вторник")
elif (k - 2) % 7 == 0:
    print("Среда")
elif (k - 3) % 7 == 0:
    print("Чеиверг")
elif (k - 4) % 7 == 0:
    print("Пятница")
elif (k - 5) % 7 == 0:
    print("Вторник")
elif (k - 6) % 7 == 0:
    print("Вторник")
