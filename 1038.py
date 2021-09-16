a, b, c, d, e = 4.00, 4.5, 5.0, 2.0, 1.5
n1, n2 = map(int, input().split())
if n1 == 1:
    print('Total: R$', '%.2f' % (a*n2))
elif n1 == 2:
    print('Total: R$', '%.2f' % (b*n2))
elif n1 == 3:
    print('Total: R$', '%.2f' % (c*n2))
elif n1 == 4:
    print('Total: R$', '%.2f' % (d*n2))
elif n1 == 5:
    print('Total: R$', '%.2f' % (e*n2))
