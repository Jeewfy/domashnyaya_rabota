'''vvod = int(input("Введите длинну стороны квадрата: "))

for i in range(vvod):
    for j in range(vvod):
        print(" * ", end='')
    print('\n')'''

def draw_tringle(fill, base=10):
    n = 1
    for i in range(base):
        i = [fill] * n
        print(''.join(i))
        n += 1

draw_tringle('*')