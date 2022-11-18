from model import Pmodel

a = Pmodel("float", 10000, -99, 99)
print(a.sum_array())
print(a.diff_array())
print(a.mult_array())
print(a.div_array())
# print(a.__dict__["array"][0])
