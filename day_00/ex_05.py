import math

def f(x):
    return math.exp(x)

left = 0
right = 1
step = 100
h = (right - left) / step

s = 0
for i in range(step):
    # Вычисление интеграла на интервале [left + i*h, left + (i+1)*h]
    x1 = (left + i*h) + (h / 2) * (-math.sqrt(3/5) + 1)
    x2 = (left + i*h) + (h / 2)
    x3 = (left + i*h) + (h / 2) * (math.sqrt(3/5) + 1)
    s += h*(5*f(x1)+8*f(x2)+5*f(x3))/18

print("Результат интегрирования трехузловым методом Гаусса:", s)
print(abs(s-(math.exp(1)-1)))
