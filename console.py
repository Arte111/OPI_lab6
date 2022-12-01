from controller import model, save

epoch = 5
amount = 575_000_000
mi = -1000
ma = 1000
t = "int"

file = save("logs/int_sum.xlsx")

for i in range(epoch):
    res = model('array', t, amount, mi, ma).sum_array()
    print(res)
    file.add_on_top([mi, ma, amount, res[0], res[1], res[2]])
