n = int(input("Введите сторону: "))
#Диагональ
#for i in range(n):
#    for j in range(n):
#        if j <= i:
#            print(" * ", end='')
#        else:
#            print(" ",end='')
#    print()
#print()

for i in range(n):
    for j in range(n):
        if j >= i:
            print(" * ", end='')
        else:
            print(" ",end='')
    print()



