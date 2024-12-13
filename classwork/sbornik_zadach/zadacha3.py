number = int(input("Введите трехзначное число: "))
desyatki = (number // 10) % 10
edinichki = number % 10
sotie = number // 100
suma = desyatki + edinichki + sotie
proizvedenie = desyatki * edinichki * sotie
print(f"в числе {number}, \n десятки - {desyatki},\n",
      f"единицы - {edinichki},\n suma - {suma}, \n произведение - {proizvedenie}")