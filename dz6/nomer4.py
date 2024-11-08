procent = 0
managers = [int(i) for i in input("Введите продажи менеджеров: ").split()]
managers = [200, 300, 600]
salaries = []
for i in managers:
    if i < 500:
        salaries.append(i + i * 0.03)
    elif i > 500 and i < 1000:
        salaries.append(i + i * 0.05)
    else:
        salaries.append(i + i * 0.08)

if salaries[0]  > salaries[1] > salaries[2]:
    print(f"лучший менеджер 1, зп:{salaries[0]+200}, {salaries[1]}, {salaries[2]}")      
elif salaries[1] > salaries[2]:
    print(f"лучший менеджер 2, зп:{salaries[1]+200}, {salaries[0]}, {salaries[2]}")      
else:
    print(f"лучший менеджер 3, зп:{salaries[2]+200}, {salaries[0]}, {salaries[2]}")
