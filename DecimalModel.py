from decimal import *
import random as rd
from time import time
from pprint import pprint

prec = 500
getcontext().prec = prec


def dec_random(a, b):
    s = str('0.' + ''.join(rd.choice('0123456789') for _ in range(prec)))
    return Decimal(a) + (Decimal(b) - Decimal(a)) * Decimal(s)


class DecimalModel:
    def __init__(self, array_type="dec", amount=None, minvalue=None, maxvalue=None):
        self.arr_time = time()
        self.array = [dec_random(minvalue, maxvalue) for i in range(amount)]
        self.arr_time = time() - self.arr_time
        self.work_time = 0

    def smart_return(self, result):
        self.work_time = time() - self.work_time
        return result, self.work_time, self.arr_time

    def sum_array(self):
        self.work_time = time()
        return self.smart_return(sum(self.array))


a = DecimalModel('dec', 1_000_000_000, 0, 1)
pprint(a.sum_array())
