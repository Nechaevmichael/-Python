# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2


n = int(input())
a = []
for i in range(-n, n + 1):
    a.append(i)
print(a)

path = 'file.txt'
data = open(path, "r")

for line in data:
    digits = line.split(' ')
data.close()
position = []
for i in range(len(digits)):
    position.append(int(digits[i]))

result = 1
for i in range(len(position)):
    result *= a[position[i]]
print(result)


# position = list(map(int, input().split(',')))

# result = 1
# for i in range(len(position)):
#     result *= a[position[i]]
# print(result)


# digits = '0 1'
# data = open('file.txt', 'w', encoding='utf-8')
# data.writelines(digits)
# data.close()




