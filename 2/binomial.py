import numpy as np
import math

class binomial_distr:
    def __init__(self, n, p):
       self.n = int(n)
       self.p = float(p)
       self.k = 0
       
       self.c = self.p/(1-self.p)
       self.r = (1-self.p)**self.n
       self.s = self.r

       self.uni = np.random.uniform(0,1, self.n)
       self.distr = []
       if self.n >= 100:
           for i in range(n):
               self.distr.append(self.bin_alg())
       else:
            self.bis_alg()
        

    def bis_alg(self):
        for nmb in self.uni:
            while nmb > self.s:
                self.k += 1
                self.r = (self.r*self.c*(self.n-self.k+1))/self.k
                self.s += self.r
                self.distr.append(self.k)


    def bin_alg(self):
        return np.random.uniform(self.n*self.p,
                                 math.sqrt(self.n*self.p*(1-self.p)))+0.5


    def bin_disp(self):
        return self.n*self.p


    def bin_math_exp(self):
        return self.n*self.p*(1-self.p)


nmb_nmb = [10, 100, 1000, 10000]
for i in nmb_nmb:
    bin_d = binomial_distr(i, 0.2)
    print('Матожидание ' + str(bin_d.bin_math_exp()))
    print('Дисперсия ' + str(bin_d.bin_disp()))
