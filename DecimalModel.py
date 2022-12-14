from joblib import Parallel, delayed
from multiprocessing import Pool
from decimal import *
from math import prod
import random as rd
from time import time
from pprint import pprint
import sys


'''f = open('choice_data.txt', 'r')

choice_data = [line.strip() for line in f]'''

choice_data = [i1 + i2 + i3 + i4 + i5 for i1 in '0123456789' for i2 in '0123456789' \
               for i3 in '0123456789' for i4 in '0123456789' for i5 in '0123456789']


# print(sys.getsizeof(dec_random(10, 100)))

class DecimalModel:

    def __init__(self, array_type="dec", amount=None, minvalue=None, maxvalue=None, prec=308):
        self.arr_time = time()
        # self.array = [dec_random(minvalue, maxvalue) for _ in range(amount)]
        # Parallel(n_jobs=-1)(delayed(dec_random)(minvalue, maxvalue) for _ in range(amount))
        self.prec = prec
        getcontext().prec = prec
        self.array = Pool().map(self.dec_random, [(minvalue, maxvalue) for _ in range(amount)])
        self.arr_time = time() - self.arr_time
        self.work_time = 0
    
    def dec_random(self, data):
        # data = [minvalue, maxvalue]
        s = str('0.' + ''.join(rd.choice(choice_data) for _ in range(self.prec//5)))
        return Decimal(data[0]) + (Decimal(data[1]) - Decimal(data[0])) * Decimal(s)

    def smart_return(self, result):
        self.work_time = time() - self.work_time
        return result, self.work_time, self.arr_time

    def sum_array(self):
        self.work_time = time()
        return self.smart_return(sum(self.array))

    def diff_array(self):
        self.work_time = time()
        return self.smart_return(-1 * sum(self.array))

    def mult_array(self):
        self.work_time = time()
        return self.smart_return(prod(self.array))

    def div_array(self):
        self.work_time = time()
        try:
            return self.smart_return(prod(self.array)**-1)
        except:
            return "of"

    def get_array(self):
        return self.__dict__["array"]

    def get_min(self):
        return min(self.array)

    def get_max(self):
        return max(self.array)


if __name__ == '__main__':
    a = DecimalModel('dec', 1_000_000, 10, 100)
    pprint(a.sum_array())
