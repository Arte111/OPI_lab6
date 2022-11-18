from time import time
import numpy as np


class Pmodel(object):
    def __init__(self, array_type="int", amount=None, minvalue=None, maxvalue=None):
        match array_type:
            case "int": self.array = np.random.randint(minvalue, maxvalue, size=(1, amount))
            case "float": self.array = np.random.uniform(minvalue, maxvalue, size=(1, amount))
        self.time = time()

    def sum_array(self):
        return np.sum(self.array), time()-self.time

    def diff_array(self):
        return -1 * self.sum_array()[0], time()-self.time

    def mult_array(self):
        return np.prod(self.array), time()-self.time

    def div_array(self):
        return 1 / self.mult_array()[0], time()-self.time
