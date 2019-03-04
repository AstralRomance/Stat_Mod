import numpy as np
import math


class uniform_distribution:
    def __init__(self, counter):
        self.min_dst = 1
        self.max_dst = 100
        self.distr = []
        self.u = []
        for i in range(counter):
            self.u = np.random.uniform(0, 1, counter)
        for k in self.u:
            self.distr.append(self.make_uniform_number(k))
        self.math_exp = 0.0
        self.disp = 0.0          
        
    def math_exp_uni(self):
        self.math_exp = (self.min_dst + self.max_dst)/2

    def dispersion_uni(self):
        self.disp = (((self.max_dst-self.min_dst+1)**2)-1)/12

    def make_uniform_number(self, nmb):
        return int((self.max_dst-self.min_dst+1)*nmb+self.min_dst)

    def write_to_file(self):
        filename = 'равномерное ' + str(len(self.distr)) + '.txt'
        f = open(filename, 'w')
        f.write('Чисел в распределении: ' + str(len(self.distr)) + '\n')
        f.write('Матожидание ' + str(self.math_exp) + '\n')
        f.write('Дисперсия ' + str(self.disp) + '\n')
        for i in self.distr:
            f.write(str(i) + ' ')
        f.close()

    

nmb_nmb = [100, 1000, 10000]
for j in nmb_nmb:
    unf = uniform_distribution(j)
    unf.math_exp_uni()
    unf.dispersion_uni()
    unf.write_to_file()
