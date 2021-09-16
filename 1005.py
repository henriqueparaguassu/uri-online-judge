n1 = float(input())
n2 = float(input())
n1, n2 = '%.1f' % n1, '%.1f' % n2
n1, n2 = float(n1), float(n2)
n1 = (n1*3.5+n2*7.5)/11
print('MEDIA =', '%.5f' % n1)
