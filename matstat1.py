import random
import math
from matplotlib import pyplot as plt
import numpy as np


def dens_dst(dst, step, pk_id):
    pr = [0 for i in range(int(1/step))]
    steps = []
    steps = np.arange(0.0, 1.1, step)
    for p in range(len(steps)-1):
        for i in dst:
            if p==0:
                if i >= steps[p] and i<steps[p+1]:
                    pr[p]+=1
            else:
                if i > steps[p] and i <= steps[p+1]:
                    pr[p]+=1
    vizual_rez(pr, pk_id, steps[0:len(steps)-1])


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
    for i in dst:
        summ2 += (i-m_w)**2
    for f in range(len(dst)):
        summ1 = 0.0
        for i in range(len(dst)-f):
            summ1 += (dst[i]-m_w)*(dst[i+f]-m_w)
        k.append(summ1/summ2)
    vizual_rez(k, graph_counter)
  

def vizual_rez(sol_array, graph_counter , plt_list = []):
    counter = [i+1 for i in range(len(sol_array))]
    fig = plt.figure(dpi = 160, figsize = (1080/160, 720/160))
    if graph_counter > 0:    
        plt.grid()
        plt.plot(counter, sol_array)
        filename = 'rez' + str(graph_counter) + '.png'
        fig.savefig(filename)
    else:
        plt.grid()
        plt.plot(plt_list, sol_array)
        filename = 'плотность' + str(graph_counter) + '.png'
        fig.savefig(filename)
        

distr_cnt = [100,1000,10000]
gk = 1
pk = -1
for i in distr_cnt:
    distr = np.random.uniform(0, 1, i)
    print('Мат ожидание '+ str(math_waiting(distr)))
    print('Дисперсия '+ str(dispersion(distr, math_waiting(distr))))
    dens_dst(distr, 0.1, pk)
    korrel(distr, math_waiting(distr), gk)
    distr.fill(0)
    gk += 1
    pk -= 1
    
