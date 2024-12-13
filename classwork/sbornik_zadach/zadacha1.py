number = int(input("Введите двухзначное число: "))
desyatki = number // 10
edinichki = number % 10
suma = desyatki + edinichki
print(f"в числе {number}, \n десятки - {desyatki},\n",
      f"единицы - {edinichki},\n suma - {suma}")