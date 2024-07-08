import math

def f(x):
    return math.exp(x)
def s(left, right, step):
    left = 0
    right = 1
    h = (right - left) / step
    s = 0
    for i in range(step):
        s += h*f(left + (i+0.5)*h)
    print("{0:<10}{1:<10}".format(step,abs(s-(math.exp(1)-1))))
left=0
right=1
step=10
        
for _ in range (7):
    s(left, right, step)
    step *= 10
