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
    while f < len(dst):
        for i in range(len(dst)-f):
            summ1 += (dst[i]-m_w)*(dst[i+f]-m_w)
        for i in dst:
            summ2 += (i-m_w)**2
        k.append(summ1/summ2)
        f+=1
    vizual_rez(k, graph_counter)
  

def vizual_rez(sol_array, graph_counter):
    counter = [i+1 for i in range(len(sol_array))]
    fig = plt.figure(dpi = 160, figsize = (1080/160, 720/160))
    print('gk is ' + str(graph_counter))
    if graph_counter == 1:    
        plt.axis([0, 100, -0.1, 0.1])
        plt.grid()
        plt.plot(counter, sol_array)
        filename = 'rez' + str(graph_counter) + '.png'
        fig.savefig(filename)
    elif graph_counter == 2:  
        plt.axis([0, 500, -0.05, 0.05])
        plt.grid()
        plt.plot(counter, sol_array)
        filename = 'rez' + str(graph_counter) + '.png'
        fig.savefig(filename)
    elif graph_counter == 3:    
        plt.axis([0, 5000, -0.004, 0.004])
        plt.grid()
        plt.plot(counter, sol_array)
        filename = 'rez' + str(graph_counter) + '.png'
        fig.savefig(filename)


distr_cnt = [100,1000,10000]
gk = 1
for i in distr_cnt:
    distr = np.random.uniform(0, 1, i)
    print('Мат ожидание '+ str(math_waiting(distr)))
    print('Дисперсия '+ str(dispersion(distr, math_waiting(distr))))
    korrel(distr, math_waiting(distr), gk)
    distr.fill(0)
    gk += 1
    
