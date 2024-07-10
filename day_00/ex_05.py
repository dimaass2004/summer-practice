import math
import matplotlib.pyplot as plt
def f(x):
    return math.exp(x)

def s(left, right, step):
    h = (right - left) / (step-1)
    s = 0
    for i in range(step-1):
        x1 = (left + i*h) + (h / 2) * (-math.sqrt(3/5) + 1)
        x2 = (left + i*h) + (h / 2)
        x3 = (left + i*h) + (h / 2) * (math.sqrt(3/5) + 1)
        s += h*(5*f(x1)+8*f(x2)+5*f(x3))/18
        return s

left = 0
right = 1
step = 10
steps = []
errors = []

for _ in range(8):
    integral_value = s(left, right, step)
    error = abs(integral_value - (math.exp(1) - 1))
    steps.append(step)
    errors.append(error)
    step *= 10

print("Step\tError")
for i in range(len(steps)):
    print(f"{steps[i]}\t{errors[i]}")

plt.plot(steps, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Количесвто разбиений')
plt.ylabel('Ошибка')
plt.title('Зависисмоть ошибки от количества разиений в трехузловом методе гауса ')
plt.grid(True)
plt.show()
