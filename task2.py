# Напишите программу, которая принимает на вход два числа и проверяет 
# является ли одно число квадратом другого.

# a = int(input())
# b = int(input())

# if a == b ** 2 or a ** 2 == b:
#     print(f'Число {a} квадрат {b}')
# else:
#     print('Не является')

# if a == b ** 2:
#     print('OK')
# elif b == a ** 2:
#     print('OK')
# else:
#     print('NO')

# Напишите программу, которая на вход принимает 5 числе и находит максимальное из них.

a = int(input())
max = a
for i in range(4):
    b = int(input())
    if b > max:
        max = b
print(max)