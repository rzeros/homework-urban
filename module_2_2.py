# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else"
first, second, third = input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: ')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
