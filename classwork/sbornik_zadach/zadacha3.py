number = int(input("Введите трехзначное число: "))
desyatki = number // 10
edinichki = number % 10
suma = desyatki + edinichki
proizvedenie = desyatki * edinichki
print(f"в числе {number}, \n десятки - {desyatki},\n",
      f"единицы - {edinichki},\n suma - {suma}, \n произведение - {proizvedenie}")