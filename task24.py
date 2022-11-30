# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


a = list(map(float, input().split()))
print(*a)

b = []
for i in range(len(a)):
    if a[i] % 1 != 0:
        b.append(round(a[i] % 1, 4))
# print(max(b))
# dig = round(max(b), 4)
# print(dig)
print(max(b) - min(b))