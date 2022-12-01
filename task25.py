# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input())

list_1 = [0, 1]
for i in range(k - 1):
    list_1.append(list_1[i] - list_1[i + 1])
list_1 = list_1[::-1]

list_2 = [0, 1]
for i in range(k - 1):
    list_2.append(list_2[i] + list_2[i + 1])

for i in range(1, k + 1):
    list_1.append(list_2[i])
print(list_1)