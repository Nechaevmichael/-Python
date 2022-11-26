# Реализуйте алгоритм перемешивания списка.

n = list(map(int, input().split()))
print(n)
import random

for i in range(len(n)):
    n[i] = n[random.randint(- 1, len(n) - 1)]
print(n)