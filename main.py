# Вводный модуль. Практические задания по уроку "Базовые структуры данных".
# 1st program
print(9**0.5*5)
# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)
# 3rd program
print(1234 % 1000 // 10 + 5678 % 1000 // 10)
# 4th program
print(int(13.42) == round(42.13 % 1 * 100) or round(13.42 % 1 * 100) == int(42.13)) # Применил функцию round() для округления из-за того, что при использовании
# остаточночного деления с другими числами, например (37.54 % 1) на выходе получал число 0.53999... вместо ожидаемых 0.54.
# (на сколько я понял, это связано с тем как числа с плавающей запятой хранятся в памяти ПК) Хотел бы услышать Ваш комментарий по данному поводу.

