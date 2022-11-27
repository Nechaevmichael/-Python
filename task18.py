# Реализуйте алгоритм перемешивания списка.

n = list(map(int, input().split()))
print(n)
import random

for i in range(len(n)):
    # n[i] = n[random.randint(- 1, len(n) - 1)]
    rand_pos = random.randint(- 1, len(n) - 1)
    n[i],n[rand_pos] = n[rand_pos],n[i]
print(n)