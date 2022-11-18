from model import Pmodel

a = Pmodel("float", 100, -99, 99)
print(a.sum_array())
print(a.diff_array())
print(a.mult_array())
print(a.div_array())

a = Pmodel("int", 100, -99, 99)
print(a.sum_array())
print(a.diff_array())
print(a.mult_array())
print(a.div_array())
# print(a.__dict__["array"][0])
