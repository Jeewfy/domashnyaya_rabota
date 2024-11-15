sec  = int(input("Введите колличество секунд: "))
hours = sec // 3600
minutes = (sec - hours * 3600) // 60
seconds = (sec - ((hours * 3600)+(minutes * 60)))
print(hours, minutes,seconds)