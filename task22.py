# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])

a = list(map(int, input().split()))
print(a)

b = []
i = 0
j = - 1
length_a = len(a) // 2
if len(a) % 2 == 0:
    for i in range(length_a):
        b.append(a[i] * a[j])
        i += 1
        j -= 1
else:
    for i in range(length_a):
        b.append(a[i] * a[j])
        i += 1
        j -= 1
    b.append(a[length_a] ** 2)

print(b)
