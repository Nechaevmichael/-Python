#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

n = list(map(int, input().split()))

temp = []
result = []
for i in n:
    if i not in temp:
        temp.append(i)
print(temp)

while len(temp) != 0:
    result.append(min(temp))
    temp.remove(min(temp))

print(result)