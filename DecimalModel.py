from decimal import *
import random as rd
from time import time
from pprint import pprint
from math import prod
from joblib import Parallel, delayed

prec = 500
getcontext().prec = prec

choice_data = [i1 + i2 + i3 + i4 for i1 in '0123456789' for i2 in '0123456789' \
               for i3 in '0123456789' for i4 in '0123456789']


def dec_random(minimal, maximum):
    s = str('0.' + ''.join(rd.choice(choice_data) for _ in range(prec // 4)))
    return Decimal(minimal) + (Decimal(maximum) - Decimal(minimal)) * Decimal(s)


class DecimalModel:
    def __init__(self, array_type="dec", amount=None, minvalue=None, maxvalue=None):
        self.arr_time = time()
        # self.array = [dec_random(minvalue, maxvalue) for _ in range(amount)]
        self.array = Parallel(n_jobs=-1)(delayed(dec_random)(minvalue, maxvalue) for _ in range(amount))
        self.arr_time = time() - self.arr_time
        self.work_time = 0

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

    def get_array(self):
        return self.__dict__["array"]

    def get_min(self):
        return min(self.array)

    def get_max(self):
        return max(self.array)


a = DecimalModel('dec', 1_000_000, 10, 100)
pprint(a.sum_array())
