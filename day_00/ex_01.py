import math
import matplotlib.pyplot as plt
def f(x):
    return math.exp(x)
def s(left, right, step):
    h = (right - left) / step
    s = 0
    for i in range(step):
        s += h * f(left + i * h)
    return s
left = 0
right = 1
step = 10
steps = []
errors = []
for _ in range(7):
    integral_value = s(left, right, step)
    error = abs(integral_value - (math.exp(1) - 1))
    steps.append(step)
    errors.append(error)
    step *= 10
print("Step\tError")
for i in range(len(steps)):
    print(f"{steps[i]}\t{errors[i]}")
plt.figure(figsize=(10, 6))
plt.plot(steps, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Количество шагов')
plt.ylabel('Ошибка')
plt.title('Завсисимость ошибки от количесва шагов в методе левых прямоугольников')
plt.grid(True)
plt.show()
