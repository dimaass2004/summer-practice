import numpy as np
def f(x):
    return np.exp(x)
x = 0
Fex = 1  

for j in range(1, 8):
    h = 10**(-j)
    F = 0
    F =  (1 / h) * (f(x + h) - f(x))  
    F = (f(x + h) - f(x))/h
    err = abs(F - Fex)
    print("Номер ", "Длина шага", "  Погрешность")
    print(j, "    ", h, "    ", err)
