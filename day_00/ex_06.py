import math

def f(x):
    return 2 * x**4 - math.sin(x) + 24 * x**6

def left_rectangle_method(left, right, step):
    h = (right - left) / step
    s = 0
    for i in range(step):
        s += h * f(left + i * h)
    return s

def central_rectangle_method(left, right, step):
    h = (right - left) / step
    s = 0
    for i in range(step):
        s += h * f(left + (i + 0.5) * h)
    return s

def trapezoid_method(left, right, step):
    h = (right - left) / step
    s = 0
    for i in range(step):
        s += h * (f(left + i * h) + f(left + (i + 1) * h)) * 0.5
    return s

methods = {
    'Left Rectangle': left_rectangle_method,
    'Central Rectangle': central_rectangle_method,
    'Trapezoid': trapezoid_method
}

left = 0
right = 1
steps = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

for step in steps:
    print(f"Step: {step}")
    for method_name, method_func in methods.items():
        integral_value = method_func(left, right, step)
        print(f"{method_name}: {integral_value}")
    print()
