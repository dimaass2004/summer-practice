import math

def f(x):
    return math.exp(x)

left = 0
right = 1
step = 10
h = (right - left) / step

s = 0
for i in range(step):
    s += h*f(left + i*h)

print("Результат интегрирования методом левых прямоугольников:", s)
print(abs(s-(math.exp(1)-1)))
