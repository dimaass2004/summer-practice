import math

def f(x):
    return math.exp(x)

left = 0
right = 1
step = 100
h = (right - left) / step

s = 0
for i in range(step):
    s += h*f(left + (i+0.5)*h)

print("Результат интегрирования методом левых прямоугольников:", s)
