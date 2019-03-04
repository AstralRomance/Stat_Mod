import numpy as np
import math

class binomial_distr:
    def __init__(self, succ, counter, p):
        self.success = succ #r
        self.count = counter #N
        self.sc_prob = p #p
        self.distr = []
        if self.count >=100:
            distr.append(binomial_2())

    def math_exp_bin(self):
        pass

    def disp_bin(self):
        pass

    def binomial_1(self, arg):
        if arg == 0:
            pass
        else:
            pass
            

    def binomial_2(self):
        return np.random.uniform(self.count * self.sc_prob,
                                 math.sqrt(self.count * self.sc_prob*(1-self.sc_prob)), 1) + 0.5
