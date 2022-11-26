# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2


# n = int(input())
# a = []
# for i in range(-n, n + 1):
#     a.append(i)

# position = list(map(int, input().split(',')))

# result = 1
# for i in range(len(position)):
#     result *= a[position[i]]
# print(result)


digits = 'Много цифр'
data = open('file.txt', 'w', encoding='utf-8')
data.writelines(digits)
data.close()