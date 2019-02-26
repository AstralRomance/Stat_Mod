import random
import math
from matplotlib import pyplot as plt
import numpy as np

def math_waiting(dst):
    summ = 0.0
    for i in dst:
        summ += i
    return summ/len(dst)


def dispersion(dst, m_w):
    summ = 0.0
    for i in dst:
        summ = (i-m_w)**2
    return summ/len(dst)


def korrel(dst, m_w, graph_counter):
    f = 1
    k = []
    summ2 = 0.0
    summ1 = 0.0
    for f in range(len(dst)):
        for i in range(len(dst)-f):
            summ1 += (dst[i]-m_w)*(dst[i+f]-m_w)
        for i in dst:
            summ2 += (i-m_w)**2
        k.append(summ1/summ2)
    file_k = open('coefficient.txt', 'w')
    vizual_rez(k, graph_counter)
    k.sort()
    for i in k:
        file_k.write(str(i) + '\n')
    file_k.close()
  

def vizual_rez(sol_array, graph_counter):
    counter = [i+1 for i in range(len(sol_array))]
    fig = plt.figure(dpi = 80, figsize = (512/80, 384/80))
    plt.axis([0, 100, -1, 1])
    plt.grid()
    plt.plot(counter, sol_array)
    filename = 'rez' + str(graph_counter) + '.png'
    fig.savefig(filename)       


gk = 1
distr = np.random.uniform(0, 1, 100)
print('Мат ожидание '+ str(math_waiting(distr)))
print('Дисперсия '+ str(dispersion(distr, math_waiting(distr))))
korrel(distr, math_waiting(distr), gk)
gk+=1
distr.fill(0)
distr = np.random.uniform(0, 1, 1000)
print('Мат ожидание '+ str(math_waiting(distr)))
print('Дисперсия '+ str(dispersion(distr, math_waiting(distr))))
korrel(distr, math_waiting(distr), gk)
gk+=1
distr.fill(0)
distr = np.random.uniform(0, 1, 10000)
print('Мат ожидание '+ str(math_waiting(distr)))
print('Дисперсия '+ str(dispersion(distr, math_waiting(distr))))
korrel(distr, math_waiting(distr), gk)
