# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

digit = int(input('Введите любое десятичное число: '))
system_of_digit = int(input('Введите систему исчисления: '))

while digit > 0:
    last = digit % system_of_digit
    print(last, end='')
    digit //= system_of_digit

