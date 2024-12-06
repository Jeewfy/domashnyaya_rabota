'''num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
list_of_number =[]

for i in range(num1, num2 + 1):
    if i == 1:
        list_of_number.append(i)
    else:
        for j in range(2, i):
            if i % j != 0:
                list_of_number.append(i)
print(set(list_of_number))'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i ==0:
            return False
    return True

def print_primes_in_range(start, end):
    print(f"Простые числа в диапазоне от {start} до {end}: ")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
    print()

start_range = int(input("Введите начальное число диапазона: "))
end_range = int(input("Введите конченое число диапазона: "))
print_primes_in_range(start_range,end_range)