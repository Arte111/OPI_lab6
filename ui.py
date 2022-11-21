# По идеи ui должен обращаться к controller, чтобы не было связей с model
# такая штука называется MVC (model view controller)
from controller import model

b = model(array_type="int", amount=1000, minvalue=-100, maxvalue=100)
a = model("float", 100000, 0, 1)
print(a.sum_array())
print(a.diff_array())
print(a.mult_array())
print(a.div_array())
print(a.get_array())
