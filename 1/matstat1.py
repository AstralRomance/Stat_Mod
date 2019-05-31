from matplotlib import pyplot as plt
import numpy as np


def dens_dst(dst, step, pk_id):
    pr = [0 for i in range(int(1/step))]
    steps = []
    steps = np.arange(0.0, 1.1, step)
    for p in range(len(steps)-1):
        for i in dst:
            if p == 0:
                if i >= steps[p] and i<steps[p+1]:
                    pr[p]+=1
            else:
                if i > steps[p] and i <= steps[p+1]:
                    pr[p]+=1
    ## График функции плотности
    kk = []
    for i in pr:
        kk.append(i/len(dst))
    plt.figure()
    plt.plot(steps[1::], kk)
    plt.savefig('Плотность' + str(len(dst)) + '.png')
    ### histogram
    plt.figure()
    plt.bar(steps[1::], pr, width=0.07)
    plt.savefig('hist.png')


def math_waiting(dst):
    summ = 0.0
    for i in dst:
        summ += i
    return summ/len(dst)


def dispersion(dst, m_w):
    summ = 0.0
    for i in dst:
        summ += (i-m_w)**2
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
    fig = plt.figure(dpi=160, figsize=(1080 / 160, 720 / 160))
    counter = [i + 1 for i in range(len(dst))]
    plt.plot(counter[1::], k[1::])
    filename = 'Кореллограмма' + str(graph_counter) + '.png'
    fig.savefig(filename)


distr_cnt = [100, 1000, 10000]
gk = 1
pk = -1
for i in distr_cnt:
    distr = np.random.uniform(0, 1, i)
    print('Мат ожидание '+str(math_waiting(distr)))
    print('Дисперсия '+str(dispersion(distr, math_waiting(distr))))
    dens_dst(distr, 0.1, pk)
    korrel(distr, math_waiting(distr), gk)
    distr.fill(0)
    gk += 1
    pk -= 1
    
plt.show()