num = (input("Введите любое четырехзначное число: "))

print("Хе хе хе я перевернул твоё число >:) --->",
      f"{int(num[3] + num[2] + num[1] + num[0])}")

print("Хе хе хе я переставил 1 и 2, 3 и 4 цифру >:) --->",
      f"{int(num[1] + num[0] + num[3] + num[2])}")

print("Хе хе хе я переставил 2 и 3 цифру >:) --->",
      f"{int(num[0] + num[2] + num[1] + num[3])}")


# вариант 1 ----------------------------------
print("Хе хе хе я переставил 1, 2 и 3, 4 цифру >:) --->",
      f"{int(num[2] + num[3] + num[0] + num[1])}")

# вариант 2 ----------------------------------
num_progress1 = int(num) // 100
num_progress2 = int(num) % 100
print("Хе хе хе я переставил 1, 2 и 3, 4 цифру >:) --->",
      f"{str(num_progress2) + str(num_progress1)}")
