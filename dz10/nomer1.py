num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
list_of_number =[]

for i in range(num1, num2 + 1):
    if i == 1:
        list_of_number.append(i)
    else:
        for j in range(2, i):
            if i % j != 0:
                list_of_number.append(i)
print(set(list_of_number))
