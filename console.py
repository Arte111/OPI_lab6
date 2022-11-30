from controller import model, save

epoch = 6
amount = 100_000_000
mi = 0.5084
ma = 1.59
t = "double"

file = save("logs/mult_double.xlsx")

for i in [model('array', t, amount, mi, ma) for i in range(epoch)]:
    mult = i.mult_array()
    file.add_on_top([mi, ma, mult[0], mult[1], mult[2]])
