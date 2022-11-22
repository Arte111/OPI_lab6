from time import time
import numpy as np


class Pmodel(object):
    def __init__(self, array_type="int", amount=None, minvalue=None, maxvalue=None):
        if array_type == "int":
            self.array = np.random.randint(minvalue, maxvalue, size=(1, amount))
        elif array_type == "float":
            self.array = np.random.uniform(minvalue, maxvalue, size=(1, amount))

        self.time = time()
        self.work_time = 0

    """ Functions for arithmetic """
    def smart_return(self, result):
        # return result (number) or error and work time
        # match-case DON'T work with -np.inf here, I don't know why
        self.work_time = time() - self.time
        if result == -np.inf:
            return "overflow -inf", self.work_time
        elif result == np.inf:
            return "overflow +inf", self.work_time
        elif result == 0.0:
            return "overflow 0.0", self.work_time
        elif result == -0.0:
            return "overflow -0.0", self.work_time
        else:
            return result, self.work_time

    def sum_array(self):
        return self.smart_return(np.sum(self.array))

    def diff_array(self):
        return self.smart_return(-1 * np.sum(self.array))

    def mult_array(self):
        return self.smart_return(np.prod(self.array))

    def div_array(self):
        return self.smart_return(1 / np.prod(self.array))

    """ Functions for trigonometry 
        return all array and time """
    def sin_array(self):
        # return np.sin(self.array)[0].tolist(), time()-self.time
        np.sin(self.array)
        return time()-self.time

    def cos_array(self):
        # return np.cos(self.array)[0].tolist(), time()-self.time
        np.cos(self.array)
        return time() - self.time

    def tan_array(self):
        # return np.tan(self.array)[0].tolist(), time()-self.time
        np.tan(self.array)
        return time() - self.time

    """ Function for all """
    def get_array(self):
        return self.__dict__["array"][0]
