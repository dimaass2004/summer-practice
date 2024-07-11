import numpy as np
import random
e=np.exp(1)

def f(x):
    return np.exp(x)

Iexact = np.exp(1) - np.exp(0)  # точное значение интеграла


for j in range(1, 8):
    N = 10**j  # число узлов
    I = 0
    n = 0
    for k in range (N):# генирирую N случайных точек
        x=random.uniform(0,1)
        y=random.uniform(0,e)
    
        y2=f(x) # значение экспоненты для х

        #a=[x,y,y2]
        #print(a)  
        if y<=y2:
            n=n+1 # считаю точки которые попали
        
        
    P=n/N
    I=(1-0)*(e-0)*P
    err = abs(I - Iexact)

    print("Номер ", "шаги", "  ошибка вычислений")
    print(j, "    ", N, "    ", err)
