import math

def f(x):
    return math.exp(x)

left = 0
right = 1
step = 100
h = (right - left) / step

s = 0
for i in range(step):
    s += h*(f(left+i*h)+ 4*f(left+h*(i+1/2))+f(left+(i+1)*h))/6

print("Результат интегрирования методом Симпсона:", s)
print(abs(s-(math.exp(1)-1)))
