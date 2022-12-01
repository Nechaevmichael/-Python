# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения (D = b^2-4ac, x1 = (-b+/- sqtr(D))/a)
    
#     2) с помощью дополнительных библиотек Python(sympy, scipy)(Дополнительно)

a = int(input())
b = int(input())
c = int(input())

import math
D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + (math.sqrt(D))/(2 * a))
    print(x1)
    x2 = (-b - (math.sqrt(D))/(2 * a))
    print(x2)
elif D == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    print('Корней не существует')

