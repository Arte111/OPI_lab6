from controller import model

amount = 300_000_000
mi = 0.501
ma = 1.59

for i in [model('array', 'double', amount, mi, ma) for i in range(6)]:
    print(i.mult_array())
