import math

def f(x):
    return math.exp(x)

def s(left, right, step):
    left = 0
    right = 1
    h = (right - left) / step
    s = 0
    for i in range(step):
        x1 = (left + i*h) + (h / 2) * (-math.sqrt(3/5) + 1)
        x2 = (left + i*h) + (h / 2)
        x3 = (left + i*h) + (h / 2) * (math.sqrt(3/5) + 1)
        s += h*(5*f(x1)+8*f(x2)+5*f(x3))/18
    print("{0:<10}{1:<10}".format(step,abs(s-(math.exp(1)-1))))
left=0
right=1
step=10
        
for _ in range (7):
    s(left, right, step)
    step *= 10
