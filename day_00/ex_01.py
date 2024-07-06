import math

def f(x):
    return math.exp(x)

left = 0
right = 1
step = 100
h = (right - left) / step

integral = 0
for i in range(step):
    integral += f(left + i*h)

integral *= h

print("Результат интегрирования методом левых прямоугольников:", integral)
