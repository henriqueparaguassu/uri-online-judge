n = float(input())
a = n
if n <= 400:
    n *= 0.15
    print("Novo salario: {}\nReajuste ganho: {}\nEm percentual: 15 %".format(
        "%.2f" % (a+n), "%.2f" % n))
elif (n > 400) and (n <= 800):
    n *= 0.12
    print("Novo salario: {}\nReajuste ganho: {}\nEm percentual: 12 %".format(
        "%.2f" % (a+n), "%.2f" % n))
elif (n > 800) and (n <= 1200):
    n *= 0.10
    print("Novo salario: {}\nReajuste ganho: {}\nEm percentual: 10 %".format(
        "%.2f" % (a+n), "%.2f" % n))
elif (n > 1200) and (n <= 2000):
    n *= 0.07
    print("Novo salario: {}\nReajuste ganho: {}\nEm percentual: 7 %".format(
        "%.2f" % (a+n), "%.2f" % n))
elif n > 2000:
    n *= 0.04
    print("Novo salario: {}\nReajuste ganho: {}\nEm percentual: 4 %".format(
        "%.2f" % (a+n), "%.2f" % n))
