import math

def f(x):
    return math.exp(x)

left = 0
right = 1
step = 10
h = (right - left) / step

s = 0
for i in range(step):
    s += h*(f(left+i*h)+ f(left+(i+1)*h))*0.5

print("Результат интегрирования методом трапеций:", s)
print(abs(s-(math.exp(1)-1)))
