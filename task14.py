n = int(input())
a = []
res = 1
for i in range(1, n + 1):
    res *= i
    a.append(res)
print(a)