from time import time
import numpy as np


class Pmodel(object):
    def __init__(self, array_type="int", amount=None, minvalue=None, maxvalue=None):
        match array_type:
            case "int": self.array = np.random.randint(minvalue, maxvalue, size=(1, amount))
            case "float": self.array = np.random.uniform(minvalue, maxvalue, size=(1, amount))
        self.time = time()

    def smart_return(self, result):
        if result == -np.inf:
            return "overflow -inf", time() - self.time
        elif result == np.inf:
            return "overflow +inf", time()-self.time
        elif result == 0.0:
            return "overflow 0.0", time()-self.time
        elif result == -0.0:
            return "overflow -0.0", time() - self.time
        else:
            return result, time()-self.time

    def sum_array(self):
        return self.smart_return(np.sum(self.array))

    def diff_array(self):
        return self.smart_return(-1 * np.sum(self.array))

    def mult_array(self):
        return self.smart_return(np.prod(self.array))

    def div_array(self):
        return self.smart_return(1 / np.prod(self.array))
