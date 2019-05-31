from matplotlib import pyplot as plt
import numpy as np
import math


def dispersion_uniform(lngt):
    return ((lngt**2)-1)/12


def math_exp_uniform(r_low, r_up):
    return (r_low+r_up)/2


def uniform_dst(r_low, r_up, lngt):
    rnd = np.random.uniform(r_low, r_up, lngt)
    dst = []
    for i in range(lngt):
        dst.append(((r_up-r_low+1)*rnd[i])+r_low)
    print(dispersion_uniform(len(dst)))
    print(math_exp_uniform(r_low, r_up))


# Общее число испытаний - lngt - N в методичке
# Число удачных испытаний - success - r в методичке
# Вероятность успеха - suc_prob - p в методичке
def dispersion_binomial(lngt, succ_prob):
    return lngt*succ_prob*(1-succ_prob)


def math_exp_binomial(lngt, succ_prob):
    return lngt*succ_prob



def binomial_dst(succ_prob, lngt):
    successs = 0
    dst = []
    if lngt < 100:
        rnd = np.random.uniform(0, 1, lngt)
        for i in range(lngt):
            if rnd[i] < succ_prob:
                successs += 1
    else:
        for i in range(lngt):
            rnd_unf = np.random.uniform(dispersion_binomial(lngt, succ_prob), math.sqrt(math_exp_binomial(lngt, succ_prob)))
            dst.append(int(rnd_unf+0.5))
    print(dispersion_binomial(lngt, succ_prob))
    print(math_exp_binomial(lngt, succ_prob))

# succ_prob - вероятность успеха, p  в методичке
def math_exp_geom(succ_prob):
    return 1/succ_prob


def dispersion_geom(succ_prob):
    return (1-succ_prob)/(succ_prob**2)


def geom_dst(succ_prob, alg):
    i = 0
    k = 0
    if alg == 0:
        while i == 0:
            rnd = np.random.uniform(0, 1)
            if rnd < succ_prob:
                i = 1
            else:
                k +=1
        print(math_exp_geom(succ_prob))
        print(dispersion_geom(succ_prob))
    elif alg == 1:
        q = 1-succ_prob
        r = succ_prob
        s = r
        rnd = np.random.uniform(0, 1)
        while rnd > s:
            k += 1
            r = r*q
            s = s+r
        print(k)
        print(math_exp_geom(succ_prob))
        print(dispersion_geom(succ_prob))
    elif alg == 2:
        rnd = np.random.uniform(0, 1)
        print(int(math.log10(rnd)/math.log(1-succ_prob)))
        print(math_exp_geom(succ_prob))
        print(dispersion_geom(succ_prob))


#
def math_exp_puass(lam):
    return lam


def dispersion_puass(lam):
    return lam


def puasson_dist(lam, alg):
    if alg == 0:
        rnd = np.random.uniform(0, 1)
        k = 0
        r = math.exp(-lam)
        s = r
        while rnd > s:
            k +=1
            r = r*(lam/k)
            s += r
        print(k)
    if alg == 1:
        rnd = np.random.uniform(0, 1)
        p = math.exp(-lam)
        i = 0
        while rnd >= p:
            rnd *= np.random.uniform(0, 1)
            i += 1
        print(i)

#
def alpha(succ_prob):
    return 1/math.log10(succ_prob)


def math_exp_log(succ_prob):
    return (-alpha(succ_prob)*(1-succ_prob))/succ_prob


def dispersion_log(succ_prob):
    return (-alpha(succ_prob)*(1-succ_prob)*(1+alpha(succ_prob)*(1-succ_prob)))/succ_prob**2


def logar_dst(succ_prob):
    print(math_exp_log(succ_prob))
    print(dispersion_log(succ_prob))



for i in [10, 100, 1000, 10000]:
    #print('UNIFORM')
    #uniform_dst(1, 100, i)
    #print('BINOMIAL')
    #binomial_dst(0.5, i)
    #print('GEOMETR')
    #geom_dst(0.5, 2)
    #puasson_dist(10, 1)
    logar_dst(0.5)