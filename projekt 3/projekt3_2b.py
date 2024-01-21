import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,10000)
x = np.zeros(len(t))

N1_0 = 3
N2_0 = 4
epsilon1, gamma1, h1 = 5, 4, 1
epsilon2, gamma2, h2 = 5, 8, 4

h = t[1]-t[0]

def N1_prim(N1, N2):
    dN1 = (epsilon1-gamma1*(h1*N1+h2*N2))*N1
    return dN1


def N2_prim(N1, N2):
    dN2 = (epsilon2-(gamma2*((h1*N1)+(h2*N2))))*N2
    return dN2


def rozw_eulerem(N1_0,N2_0):
    N1 = [N1_0]
    N2 = [N2_0]
    x1 = N1_0
    x2 = N2_0

    for i in range(len(t)):
        x1 += h*N1_prim(N1[i-1], N2[i-1])
        x2 += h*N2_prim(N1[i-1], N2[i-1])

        N1.append(x1)
        N2.append(x2)
    return N1, N2

N1, N2 = rozw_eulerem(N1_0,N2_0)
print(N1)
print(N2)

plt.plot(N1, label = "N1")
plt.plot(N2, label = "N2")
plt.xlabel("Czas")
plt.ylabel("Wartość")
plt.legend()
plt.show()

"""
Wartości maleją bardzo szybko. Nie da się dobrze zobrazować tego na wykresie.
"""