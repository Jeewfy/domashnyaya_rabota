import time

posuda = int(input("Введите колличество посуды: "))
i = 0
print("Подходим к раковине")
time.sleep(2)
print("Включаем воду")
time.sleep(2)
print("Складываем посуду в раковину")
time.sleep(2)
print("Процесс мытья посуды")
while i <= posuda:
    print("Намыливаем губку")
    time.sleep(5)
    print("Моем объект посуды...")
    time.sleep(7)
    i += 1
print("Протираем помытыю посуду")
print("Убираем помытую посуду")


