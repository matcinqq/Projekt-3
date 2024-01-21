import numpy as np
import matplotlib.pyplot as plt
from math import *

k = 100000
r = 0.4
Lambda = r

# dane przyjęte samodzielnie, potrzebne do rozwiązania zadania
t = np.linspace(0,100,1000)
x = np.zeros(len(t))
x[75] = 10
x_0 = x[75]
h = t[1]-t[0]
kroki = len(t)


def x_prim(k, r, x):
    x_prim = r*x*log(k/x)
    return x_prim


def vel(k, r, x):
    v = r*x*(1-x/k)
    return v


def rozw_rown_G(k, r, x, h, kroki):  # rozwiązanie metodą Eulera
    wyniki_g = []

    for i in range(kroki):
        wyniki_g.append(x)
        x += h*x_prim(k, r, x)

    return wyniki_g


def rozw_rown_V(k, r, x, h, kroki):  # rozwiązanie metodą Verhulsta
    wyniki_v = []

    for i in range(kroki):
        wyniki_v.append(x)
        x += h*vel(k, r, x)
    return wyniki_v


wyniki_g = rozw_rown_G(k, r, x_0, h, kroki)
wyniki_v = rozw_rown_V(k,r,x_0, h, kroki)
plt.plot(wyniki_g, label = "Rozwiązanie Gompertza")
plt.plot(wyniki_v, label = "Rozwiązanie Verhulsta")
plt.xlabel("Czas")
plt.ylabel("Objętość")
plt.legend()
plt.show()



