import math
# Заданные массивы
sin = [0.0128, 0.0256, 0.0346, 0.0461, 0.0602]
a = [0.07, 0.16, 0.25, 0.325, 0.43]
result = []
for i in range(5):
        result.append(sin[i] * a[i])
f = sum(result)-((sum(sin)*sum(a))/5)
square = [ x ** 2 for x in sin ]
k = sum(square) - (sum(sin) ** 2) / 5
B = f/k


A = (sum(a) - B * sum(sin)) / 5


d = []
for o in range(5):
        d.append(a[o] - (A + B * sin[o]))
square2 = [ y ** 2 for y in d]
D = sum(square) - ((sum(sin) ** 2 ) / 5)
sigma = ( sum(square2) / (D * 3) ) ** 0.5
print(B)





