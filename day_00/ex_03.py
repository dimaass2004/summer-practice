import math

def f(x):
    return math.exp(x)

left = 0
right = 1
step = 100
h = (right - left) / step

s = 0
for i in range(step):
    s += h*(f(left+i*h)+ f(left+(i+1)*h))*0.5

print("Результат интегрирования методом трапеций:", s)
